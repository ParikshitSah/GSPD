from attendance import main as attendance_main
import scrape
import time
from selenium import webdriver



# Xpath to First and Last Names on the attendance webpage
last_prompt = "//table/tbody/tr/td[2]//a"
first_prompt = "//table/tbody/tr/td[3]//font"
# Enter webpage link here
link = "https://gspd.gosignmeup.com/admin/courses_attendance_detail.asp?cid=4056&coursetype=0"

# log in to GSMU admin webpage
scrape.login()
# Get the First and Last Names
First_name = scrape.get_name(first_prompt, link)
Last_name = scrape.get_name(last_prompt, link)
scrape.close_browser()

# print("Last names: ", len(Last_name), "First Names: ", len(First_name))


def export_list(First_name, Last_name):
    """
    Takes the fist and last name list and converts them into one dict with indexed values for first and last names
    This will be used by the name matching module

    """
    conv_f = dict(enumerate(First_name))
    conv_l = dict(enumerate(Last_name))

    gNames = {"first": {}, "last": {}}

    gNames["first"] = conv_f
    gNames["last"] = conv_l

    
    return gNames

def take_attendance():
    result = attendance_main()
    print("Marking Attendees ... ⌛")
    

take_attendance()
