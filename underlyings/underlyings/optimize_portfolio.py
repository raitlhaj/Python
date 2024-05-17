from underlyings.basket import Basket
from underlyings.stock import Stock
from underlyings.index import Index
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog
from scipy.optimize import minimize
from math import log

def optimize_portfolio(basket: Basket, start_date: str, end_date: str, x_min= 0.00001, x_max=0.75, vol_max= 0.75, islog = False):
    #init   
    col = 0
    all_refs = basket.references
    nb_compo = len(basket.references)
    
    matrix_correl = np.zeros(shape = (nb_compo, nb_compo))
    matrix_covar = np.zeros(shape = (nb_compo, nb_compo))
    betas = np.zeros(shape = (1, nb_compo))
    matrix_vols = np.zeros(shape = (1, nb_compo))
    
    idx_bench_quotes = Index(all_refs[0]).get_quotes(start_date, end_date)
    len_idx = len(idx_bench_quotes)
    
    matrix_returns = np.zeros(shape = (len_idx - 1, nb_compo ))

    matrix = np.zeros(shape = (len_idx , nb_compo ))
    matrix[:, col] = np.transpose(idx_bench_quotes[0: len_idx])
    
    #components
    for ticker in all_refs[1:]:
      col = col + 1
      try:
        compo_quotes = Stock(ticker).get_quotes(start_date, end_date)    
        matrix[:, col] = np.transpose(compo_quotes[0: len_idx ])
      except:
        print("/!\ Can't load stock: " + str(ticker))

    for i in range(len_idx - 1):
      for j in range(nb_compo):
        
        try :
          if(islog):
            matrix_returns[i][j] = log(matrix[i + 1][j] / matrix[i][j])
          else:
            matrix_returns[i][j] = matrix[i + 1][j] / matrix[i][j]          
        except:
          print("/!\ Index Quotes length: " + str(len_idx))
          print("/!\ Compo length: " + str(nb_compo))
          print("/!\ Compo Quotes length: " + str(len(matrix)))
          print("/!\ Return Quotes length: " + str(len(matrix_returns)))
    
    vec_returns = np.prod(matrix_returns, axis = 0) - 1
    benchmark_return = vec_returns[0]

    for j in range(nb_compo):    
      matrix_vols[0][j] = np.std(matrix_returns[:, j])
    
    tmp = np.transpose(matrix_returns)
    matrix_correl = np.corrcoef(tmp)
    matrix_covar = np.cov(tmp)
    S_0 = np.sum(matrix_covar[:,0])
    
    for j in range( nb_compo): 
       betas[0][j] = np.sum(matrix_covar[:,j]) / S_0

    print("\nVector_returns:\n"+str(vec_returns))
    print("\nVols:\n"+str(matrix_vols[0]))
    print("\nCorrels:\n"+str(matrix_correl))
    print("\nCovariance:\n"+str(matrix_covar))
    print("\nBeta:\n"+str(betas[0]))
    
    ##################### init-convergence ##############################
    vec_weights = np.zeros( shape = (1, nb_compo)) + 1 / nb_compo
    vec_returns = - np.array(vec_returns[1:nb_compo])
    # Define the bounds
    bounds = np.array([(x_min, x_max)]*(nb_compo-1))   
    #Covariance
    covar_matrix = matrix_covar[1:nb_compo, 1:nb_compo] 
    vec_weights = vec_weights[0, 1:nb_compo]
    vec_vols = matrix_vols[0, 1:nb_compo]
    vol_benchmark = matrix_vols[0, 0]
  
    # Set the coefficients of the linear objective function vector
    # Note: when maximizing, change the signs of the c vector coefficient
  
    #Objective : 1
    def objective(x):
      return  np.matmul(x, np.transpose(vec_returns))
    
    #Contraints : 3
    def constraint(x):
         return x
       
    def sumOfWieghtsConstraint(x):
     return np.sum(x) - 1
    
    def volConstraint(x):
     return - np.sqrt(np.matmul(x, np.matmul(covar_matrix, x))) + vol_max

 
    # Call the minimize function to solve the optimization problem
    print(all_refs[1:])
    res = minimize(objective, vec_weights, method = 'SLSQP', bounds = bounds,
                    constraints=[{'type': 'ineq', 'fun': constraint},
                                  {'type': 'ineq', 'fun': volConstraint},
                                  {'type': 'eq', 'fun': sumOfWieghtsConstraint}])
    
    vol_folio = np.sqrt(np.matmul(res.x, np.matmul(covar_matrix, res.x)))
    return_folio = - res.fun
    
    print("Vol: "+ str(vol_folio))
    print('\nExpected Return:', round(return_folio , ndigits = 4),
    '\nx weights:', res.x,
    '\nNumber of iterations performed:', res.nit,
    '\nStatus:', res.message)       
    
    # Plot(0) Create a figure with two subplots
    fig, axs  = plt.subplots(4,1, figsize = (20, 20))
    
    df_1 = 0
    df_2 = 0
        
    for i in range(nb_compo - 1):
      axs[0].plot(matrix_returns[:, i], label = all_refs[i])
      df_1 += matrix_returns[:, i] * res.x[i]
      
    axs[0].plot(df_1, label = "FolioReturn")
    axs[0].set_xlabel('Points')
    axs[0].set_ylabel('Returns')
    axs[0].set_title(f'Return/Vol from {start_date}')
    axs[0].legend()

    # Plot(1) the second graph
    for i in range(nb_compo - 1):
      axs[1].scatter(vec_vols[i], - vec_returns[i])
   
    axs[1].scatter(vol_benchmark, benchmark_return)
    axs[1].annotate(all_refs[0], (vol_benchmark, benchmark_return), textcoords = "offset points", xytext = (0, 0.05), ha = 'center')
    axs[1].scatter(vol_folio, return_folio)
    axs[1].annotate("Folio", (vol_folio, return_folio), textcoords = "offset points", xytext = (0, 0.05), ha = 'center')

    for i, label in enumerate(all_refs[1:]):
       axs[1].annotate(label, (vec_vols[i], - vec_returns[i]), textcoords = "offset points", xytext = (0, 0.2), ha = 'center')

    axs[1].set_xlabel('Vol')
    axs[1].set_ylabel('Return')
    axs[1].set_title(f'Avreage Return/Vol between {start_date}')
    axs[1].legend()
    
    # Plot(2) the second graph
    for i in range(nb_compo - 1):
     axs[2].plot(matrix[:, i+1] / matrix[0, i+1], label = all_refs[i+1])
     df_2 += ( matrix[:, i+1] / matrix[0, i+1] ) * res.x[i]
     
    axs[2].plot(matrix[:,0] / matrix[0, 0], label = all_refs[0])
    axs[2].plot(df_2, label = "Basket")
    axs[2].set_xlabel('X')
    axs[2].set_ylabel('S')
    axs[2].set_title(f'Std-Quotesfrom {start_date}')
    axs[2].legend()
    
    # Plot(3) the second graph
    axs[3].bar(all_refs[1:], res.x)
    axs[3].set_xlabel('S(i)')
    axs[3].set_ylabel('W(i)')
    axs[3].set_title( 'Weigths')
    axs[3].legend()
    
    plt.xticks(rotation = 'vertical')
    plt.tight_layout()
    plt.show()

    return Basket(references = all_refs[1:], weights = res.x)
