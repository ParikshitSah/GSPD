
from dotenv import load_dotenv  # for python-dotenv method
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
load_dotenv()  # for python-dotenv method


def login():
    driver.get("http://gspd.gosignmeup.com/admin")

    # Find the username and password fields
    #Temporary Method to login > will probably make a branch and merge later

    Form = driver.find_element(By.TAG_NAME, "form")
    User = Form.find_element(By.NAME, 'name').send_keys(
        os.environ.get('Username_GSMU'))
    Pass = Form.find_element(By.NAME, 'pass').send_keys(
        os.environ.get('Password_GSMU') + Keys.ENTER)


def get_name(prompt , link):


        driver.get(link)
        Name = driver.find_elements(By.XPATH, prompt)
        result = []
        for i in Name:
            if(i.text != "First Name"):
                result.append(i.text)
        return result

def close_browser():
    driver.quit()

