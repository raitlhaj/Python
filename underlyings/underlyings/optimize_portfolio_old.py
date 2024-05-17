#scrapping
import pandas as pd
import openpyxl as xl
from openpyxl.chart import BarChart,Reference
from pathlib import Path
import requests
from datetime import datetime, timedelta
import investpy
import numpy as np

def yesterday(frmt = '%m/%d/%Y', string = True):
    yesterday = datetime.now() - timedelta(1)
    if string:
        return yesterday.strftime(frmt)
    return yesterday

dicto = investpy.stocks.get_stocks(country = 'united states')

for col in range(1,10):
        
    ticker = dicto['symbol'][col]
    
    try:
        
        country = 'united states'
        url = "http://api.scraperlink.com/investpy/?email=ait_lhaj92@live.fr&type=historical_data&product=stocks&country="+str(country)+"&symbol="+str(ticker)+"&from_date=01/01/2019&to_date="+yesterday()
        response = requests.get(url)
        resp_dict = response.json()
        
    except:           
        try:
            country = dicto[dicto['symbol']==ticker].iloc[0]['country']
            url = "http://api.scraperlink.com/investpy/?email=ait_lhaj92@live.fr&type=historical_data&product=stocks&country="+str(country)+"&symbol="+str(ticker)+"&from_date=01/01/2019&to_date="+yesterday()
            response = requests.get(url)
            resp_dict = response.json() 
        except: 
            print(country + ": "+ ticker +" => KO")
            continue
    
    print(country + ": " + ticker + " => OK")
    df = pd.DataFrame(resp_dict.get('data'))
    df_new = pd.DataFrame(df['last_close'])
    df_new.rename( columns = {'last_close': ticker} , inplace = True )

#return
    returns = [(float(df_new[ticker][row +1])/float(df_new[ticker][row]))   for row in range(1, len(df_new)-1)]
    returnsPeriod = [returns]
    df_return_new = pd.DataFrame(returns, columns = [ticker])
    
    if(col > 1 ):
      df_old = pd.concat([df_old, df_new], axis = 1)
      df_return_old = pd.concat([df_return_old, df_return_new], axis = 1)

    else:
        df_return_old = df_return_new
        df_old = df_new
    
print(df_old)
print(df_return_old)