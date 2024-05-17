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
import investpy
from random import *

class Stock:
    
    def __init__(self,  ticker : str) -> None:
        self.ticker = ticker
    
    def get_quotes(self, start_date: str, end_date: str):
        
        dicto = investpy.stocks.get_stocks(country = 'united states')
        chaine = "" 
       
        try:
             country='united states'
             url = "http://api.scraperlink.com/investpy/?email=ait_lhaj92@live.fr&type=historical_data&product=stocks&country="+str(country)+"&symbol="+str(self.ticker)+"&from_date="+str(start_date)+"&to_date="+str(end_date)
             response = requests.get(url)
             resp_dict = response.json()
        except:
            
            try:
                country=dicto[dicto['symbol']==self.ticker].iloc[0]['country']
                url = "http://api.scraperlink.com/investpy/?email=ait_lhaj92@live.fr&type=historical_data&product=stocks&country="+str(country)+"&symbol="+str(self.ticker)+"&from_date="+str(start_date)+"&to_date="+str(end_date)
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
               
    def is_compliant(self):

        option = webdriver.ChromeOptions()
        option.binary_location = r"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

        driver = webdriver.Chrome(
            executable_path = r'C:\\Users\\Administrateur\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe',
            options = option)
        
        driver.get("https://finispia.com/")
        ticker = self.ticker
        text_input = driver.find_element(By.ID, 'search')
        text_input.send_keys(ticker)

        wait = WebDriverWait(driver,10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'autocomplete-results')))

        autocomplete_result = driver.find_element(By.XPATH, f'//ul[@class="autocomplete-results"]/li[contains(span[@class="ticker"],"{ticker}") and contains(span[@class="nation"]/text(),"USA")]')
        autocomplete_result.click()

        time.sleep(5)
        
        cmp_state_element = driver.find_element(By.XPATH, "//div[@class='cmpState']")
        cmp_rate_element = driver.find_element(By.XPATH, "//div[@class='rate']")
        cmp_rateLimit_element = driver.find_element(By.XPATH, "//div[@class='rateLimit']")
        # Extract the text from the element
        cmp_state = cmp_state_element.text

        # Print the cmpState
        print(cmp_state_element.text)
        print(cmp_rate_element.text + cmp_rateLimit_element.text)