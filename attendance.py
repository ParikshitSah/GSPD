# Could have used regex and avoided 90% of the stuff done here but YOLO

from prettytable import PrettyTable
from scrape import export_list, scrape_names
from user_pts import *
from excel import read_file
import math
final_list = []


# Tetsung

x = PrettyTable()
p = PrettyTable()

p.field_names = ["ID", "First Name", "Last Name", "⌛  Partial Match"]
x.field_names = [
    "ID", "First Name", "Last Name", " ✅ Full Match"
]

Scrape = scrape_names()
First = Scrape[0]
Last = Scrape[1]
gNames = export_list(First, Last)



# create list with excel names
excelNamesUnfiltered  = read_file("Name (Original Name)", "./2.15.2023 Personal Branding.csv")


excelNames = [*set(excelNamesUnfiltered)
                ]  # only unique values from excel names




KeyValues = {"Matches": {}, "Partial Matches": {}}



def cosine_similarity(s1, s2):
    """Calculate the cosine similarity of two strings

    Args:
        s1 (string): gName first + last value
        s2 (_type_): Excel Value

    Returns:
        int: similarity from 0 to 1
    """
    vec1 = {c: s1.count(c) for c in set(s1)}
    vec2 = {c: s2.count(c) for c in set(s2)}
    dot_product = sum(vec1[c] * vec2.get(c, 0) for c in vec1)
    norm1 = math.sqrt(sum(v ** 2 for v in vec1.values()))
    norm2 = math.sqrt(sum(v ** 2 for v in vec2.values()))
    return dot_product / (norm1 * norm2)


def find_matches(baseVal):
    """Uses the cosine similarity to calculate string similarity

    Args:
        baseVal float: minimum similarity for partial match
    """
    
    maxNum = len(gNames["first"])
    
    
    for i in range(0,maxNum):
        for name in excelNames:
            real = f"{gNames['first'][i]} {gNames['last'][i]}"
            similarity = cosine_similarity(real.lower().strip(), name.lower().strip())
            if similarity > baseVal :
                if similarity > 0.89:
                    
                    KeyValues["Matches"].setdefault(i, []).append(excelNames.index(name))
                    
                    print(f"✅ matched {real} index {i} with {name} index {excelNames.index(name)}")
                else:
                   
                    KeyValues["Partial Matches"].setdefault(i, []).append(excelNames.index(name))
                
                    print(f"🎈Partially matched {real} index {i} with {name} index {excelNames.index(name)}")
                    
    
                    
            
            
            
            
    
    
        

def lxt(index):
    """Converts IDs from a list to table with first and last names

    Args:
        index (list): contains index for gNames dict

    Returns:
        Table: table from prettytable
    """
    names = PrettyTable()
    names.field_names = ["ID","Last Name", "First Name"]
    total = PrettyTable()
    total.padding_width = 5
    total.header = False
    total.field_names = ["1", "2"]
    length = len(index)
    total.add_row(["Total Participants", length])
    for i in index:
        names.add_row([i,gNames['first'][i], gNames['last'][i]])
    return names.get_string(sortby= "ID"), total.get_string()



def show_results():
    """ 
    Add values to the perfect match table 
    """
    for i in KeyValues["Matches"]:
        for indexofarray in [*set(KeyValues["Matches"][i])]:
            x.add_row([
                indexofarray, gNames["first"][indexofarray], gNames["last"][indexofarray],
                excelNames[indexofarray]
            ])
            final_list.append(indexofarray)
            
            
    

    """
    Add values to the partial match table. Adds the ID, First Name, Last Name and Excel Names
    """

    for i in KeyValues["Partial Matches"]:
        for indexofarray in [*set(KeyValues["Partial Matches"][i])]:
            p.add_row([
                indexofarray, gNames["first"][indexofarray], gNames["last"][indexofarray],
                excelNames[indexofarray]
            ])
    x.sortby = "ID"
    p.sortby = "ID"
    r = PrettyTable()
    r.field_names = ["🧮 Total perfect matches:", '{:0>2}'.format(
        len(x.rows)), "⌛ Total partial matches:", '{:0>2}'.format(len(p.rows))]

    # Print perfect matches
    print(x.get_string())
    # Print Partial Matches
    print(p.get_string())
    # Print Results
    print(r.get_string())

find_matches(0.7)

# show_results()
# dup_list = final_list.copy()
# MVP working for deleting names
# row_count = len(x.rows)

def update_list(func, amend_list):
    """Calls function from user_pts.py to 
    add or delete values to the duplicate list

    Args:
        func (function): add or delete function?
        amend_list (list): takes a copy of the final list

    Returns:
        None: _description_
    """
    
    max_final_list = len(gNames['first'])
    user_edit = get_list(max_final_list)
    for i in user_edit:
        if (func == "DEL"):
            try:
                list_delete(i, amend_list)
            except ValueError:
                print(
                    f"error number {i} already not in list, check table again!")
                continue

        elif (func == "ADD"):
            try:
                list_add(i, amend_list)
            except ValueError:
                print(
                    f"error number {i} already in list, check table again!")
                continue

def change_list():
    """Implements changes to a duplicate list of the final list created earlier. This is done to so that changes can 
    be reverted if needed.
    """
    

    response = make_edits()

    if (response == "Cancel" or response == "exit"):
        print("Exiting Edit")
        return "exit"

    # Adding to the list
    elif (response == "Add"):
        update_list("ADD", dup_list)

    # Deleting from the list
    elif (response == "Delete"):
        update_list("DEL", dup_list)

    elif (response == "Revert To Orignal List"):
        print("Confirm changes? All changes made will be lost")
        if pyip.inputYesNo() == 'yes':
            return final_list
        else:
            return dup_list

    print("✅ Here's the final table select options below ✅")
    print(lxt(dup_list)[0])
    return dup_list



def make_final_list():

    print("Make edits to the list [y/n]")
    more_edits = pyip.inputYesNo()

    curr = final_list.copy()

    if (more_edits == "no"):
        # confirm and push changes
        print("✅ Here is the final list of attendes that will be marked ✅")
        print(lxt(final_list)[0])
        print("Confirm Attendence? [y/n]")
        if (pyip.inputYesNo() == "yes"):
            print("confirmed")
            return
        else:
            print("cancelled")
        return
    else:
        # loop while user wants to no more make changes

        while more_edits == "yes":
            run = change_list()
            if (run == "exit"):
                more_edits = "no"
            else:
                curr = run

    return curr


