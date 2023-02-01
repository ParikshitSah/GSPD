import pyinputplus as pyip


def user_edit_prompt():

    print("Do you want to edit the perfect matches list? [y/n] ")
    edit = pyip.inputYesNo()
    return edit


def make_edits():
    answer = user_edit_prompt()
    delete, add = False, False

    if (answer):
        print("ask if delete or edit")
        if (delete):
            print('start delete prompts')
        if (add):
            print("start add prompts")
        else:
            print("confirm for cancel")
