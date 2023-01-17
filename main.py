import scrape
import time

first_prompt = "//table/tbody/tr/td[2]/a"
last_prompt = "//table/tbody/tr/td[3]//font"
# Enter webpage link here
link = "https://gspd.gosignmeup.com/admin/courses_attendance_detail.asp?cid=3786&coursetype=0" 

scrape.login()

First_name = scrape.get_name(first_prompt, link)
Last_name = scrape.get_name(last_prompt, link)

print(First_name, Last_name)

