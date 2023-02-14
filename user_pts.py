import pyinputplus as pyip
import re


def user_edit_prompt():

    print("Do you want to edit the perfect matches list? [y/n] ")
    edit = pyip.inputYesNo()
    return edit


def make_edits():
    answer = user_edit_prompt()

    if (answer == "no"):
        return "exit"
    else:
        response = pyip.inputMenu(["Add", "Delete", "Cancel"], numbered=True )
        return response

def list_delete(num, list):
    """Removes number from the list

    Args:
        num (int): number in the final list
    """
    if num in list:
        list.remove(num)
        return True
    else:
        raise ValueError("Number already not in list or out of range")
    
def list_add(num, list):
    """adds number to the list

    Args:
        num (int): number in the final list
    """
    if num not in list:
        list.append(num)
        return True
    else:
        # Number already in list or out of range
        raise ValueError("Number already in list or out of range")
        
def get_list(max_num):
    print("Enter the index numbers separated by commas. Do NOT end with comma")
    print("Note: if the number entered is out of range it will be skipped")
    print("Example: 1,2,3,4")
    ans = input("Enter here: ")
    numbers = re.split(',', ans)
    
    result = []
    for number in numbers:
        if number == '':
            # Skip empty strings
            continue
        
        try:
            converted_number = int(number)
            result.append(converted_number)
        except ValueError:
            # If the string cannot be converted to an integer, just skip it
            continue
        if not (0 <= converted_number <= max_num):
            # If the converted number is not within the desired range, skip it
            continue
    return result

