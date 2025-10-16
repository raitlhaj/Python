from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import requests
import investpy
from random import *
from multiprocessing import Process, Queue
from utils.utils.files import stocks_url_to_scrap, brower_path, chrome_driver_path, fini_url_search, fini_url_login
from utils.utils.passwords import MY_PASSWORD, MY_USERNAME

class Stock:
    
    def __init__(self,  ticker : str) -> None:
        self.ticker = ticker
    
    def get_quotes(self, start_date: str, end_date: str):
        
        dicto = investpy.stocks.get_stocks(country = 'united states')
        chaine = "" 
    
        try:
            country='united states'
            url = stocks_url_to_scrap + str(country)+"&symbol="+str(self.ticker)+"&from_date="+str(start_date)+"&to_date="+str(end_date)
            response = requests.get(url)
            resp_dict = response.json()
        except:
            
            try:
                country=dicto[dicto['symbol']==self.ticker].iloc[0]['country']
                url = stocks_url_to_scrap + str(country)+"&symbol="+str(self.ticker)+"&from_date="+str(start_date)+"&to_date="+str(end_date)
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
            
    def is_compliant(self, tickers = None):

        if tickers is None :
            tickers = [self.ticker]
              
        # Set up options for Brave browser
        option = webdriver.ChromeOptions()
        option.binary_location = brower_path  # Path to Brave browser executable
        service = Service(chrome_driver_path)  # Path to ChromeDriver executable
        driver = webdriver.Chrome(service=service, options=option)
        driver.get(fini_url_login)

        # Locate the username and password fields and enter credentials
        username_field = driver.find_element(By.NAME, 'email')  # Adjust the element identifier as needed
        password_field = driver.find_element(By.NAME, 'password')  # Adjust the element identifier as needed

        username_field.send_keys(MY_USERNAME)
        password_field.send_keys(MY_PASSWORD)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for the login process to complete (adjust the time if necessary)
        

        def f(slef, q):
            q.put(self.tickers)

     
        def H(self, ticker):
            time.sleep(5) 
            driver.get(fini_url_search)
            time.sleep(5) 

            text_input = driver.find_element(By.NAME, 'company')
            text_input.send_keys(ticker)
            wait = WebDriverWait(driver,20)
            dropdown = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'dropdown.open.dropdown-menu')))
            # Locate all dropdown items
            dropdown_items = dropdown.find_elements(By.CLASS_NAME, 'dropdown-item')

            # Iterate through the items and print their text
            for item in dropdown_items:
                if 'USA (NASDAQ)' in item.text:
                    item.click()
                    break
                
            time.sleep(10)
            cmp_state_element = driver.find_element(By.XPATH, "//div[@class='box compliance']")

            # Print the cmpState
            cmpState = ticker+(" Halal: " if int(cmp_state_element.text[0]) > 0 else " NonHalal: " )+ cmp_state_element.text

            print(cmpState)
        
        print("Starting ....")
        
        q = Queue()
        p = Process(target=f, args=(q,))
        p.start()
        H(q.get())  
        p.join()
        





