import time
from dotenv import load_dotenv  # for python-dotenv method
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
load_dotenv()  # for python-dotenv method

def main():


    # Navigate to the login page
    driver.get("http://gspd.gosignmeup.com/admin")

    # Find the username and password fields
    Form = driver.find_element(By.TAG_NAME, "form")
    User = Form.find_element(By.NAME, 'name').send_keys(
        os.environ.get('Username_GSMU'))
    Pass = Form.find_element(By.NAME, 'pass').send_keys(
        os.environ.get('Password_GSMU') + Keys.ENTER)

    #Temporary Method to get names

    driver.get("https://gspd.gosignmeup.com/admin/courses_attendance_detail.asp?cid=3786&coursetype=0")

    # Getting First Names
    # Table > tbody > tr > td > a (First Name)
    Table = driver.find_elements(By.TAG_NAME, "table")
    
    

    for i in Table:
        Names = i.find_elements(By.TAG_NAME, "a")
        for e in Names:
            print(e.text)

    # Body = Table.find_element(By.TAG_NAME, "tbody")
    # Tr = Body.find_element(By.TAG_NAME, "tr")

    time.sleep(500)

    


main()
