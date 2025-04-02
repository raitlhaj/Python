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


class RunIT:
    
    def __init__(self) -> None:
        pass
            
    def is_compliant(self):

                
        # Set up options for Brave browser
        option = webdriver.ChromeOptions()
        option.binary_location = r"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        service = Service('C:\\Users\\Administrateur\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=option)
        driver.get("https://fr.tlscontact.com/visa/ma/maRAK2fr/home")

        # Locate the username and password fields and enter credentials
        username_field = driver.find_element(By.NAME, 'email')  # Adjust the element identifier as needed
        password_field = driver.find_element(By.NAME, 'password')  # Adjust the element identifier as needed

        # Enter your username and password
        username = 'khadijaonaceur1997@gmail.com'  # Replace with your actual username
        password = 'DijaVisa@2024'  # Replace with your actual password

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for the login process to complete (adjust the time if necessary)
        

        def f(slef, q):
            q.put()

     
        def H(self ):
            time.sleep(5) 
            driver.get("https://app.finispia.com/company/search/")
            time.sleep(5) 

            text_input = driver.find_element(By.NAME, 'company')
            text_input.send_keys()
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
        





