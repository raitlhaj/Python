from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time
import pandas as pd
import requests
import investpy
import pandas as pd
import requests
import investpy
from random import *
import openpyxl as xl


class Index:
    
    def __init__(self,  ticker : str) -> None:
        self.ticker = ticker
    
    def get_quotes(self, start_date: str, end_date: str):
        
        dicto = investpy.indices.get_indices(country = 'united states')
        chaine = "" 
       
        try:
             country='united states'
             url = "http://api.scraperlink.com/investpy/?email=ait_lhaj92@live.fr&type=historical_data&product=indices&country="+str(country)+"&symbol="+str(self.ticker)+"&from_date="+str(start_date)+"&to_date="+str(end_date)
             response = requests.get(url)
             resp_dict = response.json()
        except:
            try:
                country=dicto[dicto['symbol']==self.ticker].iloc[0]['country']
                url = "http://api.scraperlink.com/investpy/?email=ait_lhaj92@live.fr&type=historical_data&product=indices&country="+str(country)+"&symbol="+str(self.ticker)+"&from_date="+str(start_date)+"&to_date="+str(end_date)
                response = requests.get(url)
                resp_dict = response.json()              
            except: 
                chaine = str(chaine) + country + ": "+self.ticker+ "=> KO \n"
        
        chaine = str(chaine) + country + ": "+ self.ticker + "=> OK \n"
        df = pd.DataFrame(resp_dict.get('data'))
        df_new = pd.DataFrame(df['last_close'])
        df_new.rename(columns = {'last_close': self.ticker} , inplace = True )
        
        df_new = df_new.apply(lambda x: x.str.replace(',',''))
        
        #Revese
        df_new = df_new[::-1]
        df_new = df_new.reset_index(drop=True)
        
        return df_new.astype('float64')
               