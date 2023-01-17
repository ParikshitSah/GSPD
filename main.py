import scrape
import time

last_prompt = "//table/tbody/tr/td[2]"
first_prompt = "//table/tbody/tr/td[3]//font"
# Enter webpage link here
link = "https://gspd.gosignmeup.com/admin/courses_attendance_detail.asp?cid=3860" 

scrape.login()

First_name = scrape.get_name(first_prompt, link)
Last_name = scrape.get_name(last_prompt, link)

print(Last_name, len(Last_name))

