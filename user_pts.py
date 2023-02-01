import pyinputplus as pyip
 
 
def user_edit_prompt():

    print("Do you want to edit the perfect matches list? [y/n] ")
    edit = pyip.inputYesNo()
    return edit