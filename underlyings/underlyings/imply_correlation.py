from underlyings.basket import Basket
from underlyings.stock import Stock
from underlyings.index import Index

import numpy as np

def imply_correl( my_idx : str, basket : Basket , start_date: str, end_date: str) -> float:
    
    #init 
    compo =  basket.references
    weights = basket.weights
    col = 0
    nb_ticker = len(compo)
    
    #index 
    idx_quotes = Stock(my_idx).get_quotes(start_date, end_date)
    len_idx = len(idx_quotes) - 1
    matrix = np.zeros(shape=(len_idx , nb_ticker + 1))
    matrix[:,col] = np.transpose(idx_quotes[0:len_idx])
    
    #components
    for ticker in compo :
      col = col + 1
      compo_quotes = Stock(ticker).get_quotes(  start_date, end_date)
      matrix[:,col] = np.transpose(compo_quotes[0:len_idx])
    
    vol_idx  = np.std(matrix[:,0])
    sum_disj = 0
    sum_join = 0 
    
    for i in range(1, nb_ticker):
      for j in range(1, nb_ticker):

        if i < j :
         sum_disj =  sum_disj + weights[i] * weights[j] * np.std(matrix[:,i+1]) * np.std(matrix[:,j+1])
        if i == j :         
         sum_join =  sum_join + weights[i] * weights[j] * np.std(matrix[:,i+1]) * np.std(matrix[:,j+1])
         
    if sum_disj != 0 :
       rho_avr = (vol_idx - sum_disj)/(2 * sum_disj)
       print("Implied correlation : " + str(rho_avr))
    else:
     print("Please check basket prices !")
     rho_avr = 0

    
    return rho_avr
  

