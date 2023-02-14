import pyinputplus as pyip


def user_edit_prompt():

    print("Do you want to edit the perfect matches list? [y/n] ")
    edit = pyip.inputYesNo()
    return edit


def make_edits():
    answer = user_edit_prompt()
    response = 0

    if (answer):
        print("[1] Add ", "[2] Delete ", "[3] Cancel")
        response = pyip.inputNum('Enter number from the menu: ', min=1, max=3)
        if (response == 2):
            print('start delete prompts')
        elif (response == 1):
            print("start add prompts")
        else:
            print("confirm for cancel")
