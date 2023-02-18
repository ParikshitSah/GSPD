from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import time
from dotenv import load_dotenv  # for python-dotenv method
from scrape import login


load_dotenv()  # for python-dotenv method


def mark_attendance(ID):

    driver = webdriver.Chrome()

    link = "https://gspd.gosignmeup.com/admin/courses_attendance_detail.asp?cid=3786&coursetype=0"

    login(driver)
    
    driver.get(link)

    first = lambda j : driver.find_element(By.XPATH, f"//table/tbody/tr[{str(j)}]/td[3]//font")
    second = lambda j : driver.find_element(By.XPATH, f"//table/tbody/tr[{str(j)}]/td[2]//a")
    

    for i in ID:
       
        driver.find_element(By.XPATH, f"/html/body/center/font/table/tbody/tr[{str(i+2)}]/td[4]/font/table/tbody/tr/td/input").click()
        print(f"🤖 Marked Attendance for {first(i+2).text} {second(i+2).text}")
    
    time.sleep(100)
        





