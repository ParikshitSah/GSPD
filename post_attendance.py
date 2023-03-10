from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import os
import time
from dotenv import load_dotenv  # for python-dotenv method
from scrape import login
from paras import link

load_dotenv()  # for python-dotenv method


def mark_attendance(ID):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    login(driver)

    driver.get(link)

    first = lambda j: driver.find_element(
        By.XPATH, f"//table/tbody/tr[{str(j)}]/td[3]//font"
    )
    second = lambda j: driver.find_element(
        By.XPATH, f"//table/tbody/tr[{str(j)}]/td[2]//a"
    )

    for i in ID:
        try:
            driver.find_element(
                By.XPATH,
                f"/html/body/center/font/table/tbody/tr[{str(i+2)}]/td[4]/font/table/tbody/tr/td/input",
            ).click()
            print(
                f"\033[32m🤖 Marked Attendance for {first(i+2).text} {second(i+2).text}\033[32m"
            )
        except:
            continue

    time.sleep(100)
