
from dotenv import load_dotenv  # for python-dotenv method
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
load_dotenv()  # for python-dotenv method



# /html/body/center/font/table/tbody/tr[2]/td[4]
# Xpath to First and Last Names on the attendance webpage
last_prompt = "//table/tbody/tr/td[2]//a"
first_prompt = "//table/tbody/tr/td[3]//font"
# Enter webpage link here
link = "https://gspd.gosignmeup.com/admin/courses_attendance_detail.asp?cid=4056&coursetype=0"


# print("Last names: ", len(Last_name), "First Names: ", len(First_name))

def scrape_names():
    login(driver)
    # Get the First and Last Names
    First_name = get_name(first_prompt, link)
    Last_name = get_name(last_prompt, link)
    close_browser()
    
    return First_name , Last_name

def export_list(First_name, Last_name):
    """
    Takes the fist and last name list and converts them into one dict with indexed values for first and last names
    This will be used by the name matching module

    """
    
    # log in to GSMU admin webpage
    

    conv_f = dict(enumerate(First_name))
    conv_l = dict(enumerate(Last_name))

    gNames = {"first": {}, "last": {}}

    gNames["first"] = conv_f
    gNames["last"] = conv_l

    
    return gNames

def login(driver):
    driver.get("http://gspd.gosignmeup.com/admin")

    # Find the username and password fields
    #Temporary Method to login > will probably make a branch and merge later

    Form = driver.find_element(By.TAG_NAME, "form")
    User = Form.find_element(By.NAME, 'name').send_keys(
        os.environ.get('Username_GSMU'))
    Pass = Form.find_element(By.NAME, 'pass').send_keys(
        os.environ.get('Password_GSMU') + Keys.ENTER)
    
    return True


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


