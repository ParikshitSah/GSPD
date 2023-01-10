import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#os.environ['PATH'] += r"C:/Users/14065/OneDrive - purdue.edu/Documents/GSPD/GSPD"
driver = webdriver.Chrome()

def main():
    


# Start a browser instance
    

    # Navigate to the login page
    driver.get("http://gspd.gosignmeup.com/admin")

    # Find the username and password fields
    u = driver.find_element(By.TAG_NAME, "form")
    p = u.find_element(By.NAME, 'name').send_keys("webdriver" )
    c = u.find_element(By.NAME, 'pass').send_keys("webdriver" + Keys.ENTER)

    
   
    # password = driver.find_element(By.ID , "Password")


    time.sleep(500)
  
    # Enter the username and password
    

    # Submit the form
    

    
main()