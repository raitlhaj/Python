from investpy import *
from math import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class myStock:
    def __init__(self,name):
        self.name=name

#import matplotlib.pyplot as plt
#from investpy import *
nbOfStock=2
myCountry=get_stock_countries()
allCountryStock = get_stocks('united states')


#instruementbyisin
#search_results = search_stocks('isin', 'ES0113211835')

 #result = get_index_historical_data('DAX','united states','01/01/2020','01/06/2020','Daily','descending')
 #index=param['name'],country=param['country'],from_date='01/01/2001',to_date=today,interval=interval,order='descending')

#allCountryStock['symbol'].index
myReturn=range(nbOfStock,nbOfStock)
myDayVol=[]
myArtVol=[]


for i in range(nbOfStock):
    print(allCountryStock['symbol'][i])
    try:
        stock=get_stock_historical_data(allCountryStock['symbol'][i],'united states','01/09/2021','06/09/2021')
        #nbline=np.max(nbline,stock.size)
        #print(nbline)

        #myOpen=stock['Open']
        #myClose=stock['Close']
       #print(myClose)
       # print(myOpen)

        if i==0:
            myReturn[i]=[(myClose-myOpen)/myOpen]
            myDayVol=[np.log(myClose/myOpen)]
            myArtVol=[np.sqrt((myClose-myOpen)/myOpen)]
        else: 
            myReturn[i]=[myReturn[i],(myClose-myOpen)/myOpen]
            myDayVol=[myDayVol,np.log(myClose/myOpen)]
            myArtVol=[myArtVol,np.sqrt((myClose-myOpen)/myOpen)]      
    except:
        print(IndentationError)
        print("There's error here!") 
 
print(myReturn)



    #l=stock.to_dict('list');
    #stockName=[stockName,stocks_list{i}];
    
      #  for j=1:length(l{'Open'})
      #   matriceStocks(j,i-k)=l{'Open'}{j};
      #  end

   # catch
  #      disp("Error in stock's data: "+stocks_list{i});
 #   end

   # stock.to_csv('C:\Users\Rachid\Desktop\Stocks\'+stocks_list{i}+'.csv');
   
#end

#stock=get_stock_historical_data('CVX','united states','01/01/2020','26/02/2021')
