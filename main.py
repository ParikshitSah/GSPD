from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    
    driver = webdriver.Chrome()

    driver.get("https://gspd.gosignmeup.com/Public/Course/Browse")

    Finder = driver.find_element(By.CLASS_NAME, "Welcome")
    print(Finder.text)

    driver.quit()

test_eight_components()