# Could have used regex and avoided 90% of the stuff done here but YOLO

from prettytable import PrettyTable
from scrape import export_list, scrape_names
from user_pts import *
from excel import read_file
import math
from paras import header_name, excelPath
dup_list = final_list = []


# Tetsung

x = PrettyTable()
p = PrettyTable()

p.field_names = ["ID", "First Name", "Last Name", "⌛  Partial Match", "Similarity Index"]
x.field_names = [
    "ID", "First Name", "Last Name", " ✅ Full Match"
]

Scrape = scrape_names()
First = Scrape[0]
Last = Scrape[1]
gNames = export_list(First, Last)



# create list with excel names
excelNamesUnfiltered  = read_file(header_name, excelPath)


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
            similarity = cosine_similarity(str(real).lower().strip(), str(name).lower().strip())
            
            if similarity >= baseVal :
                if similarity > 0.92:
                    
                    KeyValues["Matches"].setdefault(i, []).append(excelNames.index(name))
                    
                else:
                   
                    KeyValues["Partial Matches"].setdefault(i, []).append(excelNames.index(name))
                
            
                    
    
                    
            
            
            
            
    
    
        

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
    # values are index of gNames
    for values in KeyValues["Matches"]:
        matchedArrays  = KeyValues["Matches"][values]
        for num in matchedArrays:
            # iterate through list inside matched key and add to table
            x.add_row([values, gNames["first"][values], gNames["last"][values],excelNames[num]])
            final_list.append(values)
            dup_list.append(values)
            

    """
    Add values to the partial match table. Adds the ID, First Name, Last Name and Excel Names
    """
    
    for values in KeyValues["Partial Matches"]:
        matchedArrays  = KeyValues["Partial Matches"][values]
        for num in matchedArrays:
            # iterate through list inside matched key and add to table
            first = gNames["first"][values]
            last = gNames["last"][values]
            origN = f"{first} {last}"
            macN = excelNames[num]
            
            
            si = cosine_similarity(origN.lower().strip(), macN.lower().strip())
            p.add_row([values, gNames["first"][values], gNames["last"][values],excelNames[num], si])


    x.sortby = "ID"
    p.sortby = "Similarity Index"
    p.reversesort = True
    r = PrettyTable()
    r.field_names = ["🧮 Total perfect matches:", '{:0>2}'.format(
        len(final_list)), "⌛ Total partial matches:", '{:0>2}'.format(len(p.rows))]

    # Print perfect matches
    print(x.get_string())
    # Print Partial Matches
    print(p.get_string())
    # Print Results
    print(r.get_string())



print("duplist:",dup_list)
row_count = len(x.rows)

def update_list(func, amend_list:list):
    """Calls function from user_pts.py to 
    add or delete values to the duplicate list

    Args:
        func (function): add or delete function?
        amend_list (list): takes a copy of the final list

    Returns:
        None: _description_
    """
    # get maximum array input number
    max_final_list = len(gNames['first'])
    # ask user to enter list values 
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
        
    # Restore orignal list
    elif (response == "Revert To Orignal List"):
        print("Confirm changes? All changes made will be lost")
        if pyip.inputYesNo() == 'yes':
            return final_list
        else:
            return dup_list

    
    print("change list: ✅ Here's the final table select options below ✅")
    print(lxt(list(set(dup_list)))[0])
    return list(set(dup_list))



def make_final_list():
    """Keeps asking for edit until user cancels or reverts

    Returns:
        list: list to be marked
    """
    res = []
    while True:
        cur = change_list()
        if cur != 'exit':
            res = cur
        else:
            return list(set(res))
        



