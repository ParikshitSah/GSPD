# Could have used regex and avoided 90% of the stuff done here but YOLO

from prettytable import PrettyTable
from scrape import export_list, scrape_names
from user_pts import *

final_list = []



x = PrettyTable()
p = PrettyTable()

p.field_names = ["ID", "First Name", "Last Name", "⌛  Partial Match"]
x.field_names = [
    "ID", "First Name", "Last Name", " ✅ Full Match"
]

# Conducting a Literature Review 11/1/2022
Scrape = scrape_names()
First = Scrape[0]
Last = Scrape[1]
gNames = export_list(First, Last)

# create list with excel names
excelNamesUnfiltered = [
    'Abd Alrhman Bani Issa',
    'Abigail Erskine',
    'Alex Ozbolt',
    'Allegra Stahl',
    'Lamunu',
    'Benjamin Ayodipupo',
    'Connor Lazzaro',
    'Elvis Junior Dun-Dery',
    'Enoch Tetteh Amoatey',
    'Enoch Tetteh Amoatey',
    'Favour Ojike',
    'Francisco',
    'Francisco',
    'Mia',
    'Dikai Xu',
    'Kate Moran',
    'Christina Joslin',
    'KUNMING SHAO',
    'Yihao Chen',
    'Vlada Volyanskaya',
    'Thomas',
    'Lucas M.',
    'Jessica Veenstra',
    'Maddie Ransford',
    'Michael Cheng',
    'Michael Hansen',
    'Alma Lopez Linan',
    'Nicole Balog',
    'Eunjae Choi',
    'Ethan Potter',
    'Kendalyn Fruehauf',
    'Onni',
    'David Park',
    'Zainub',
    'nathan',
    'Toby',
    'Kyle Andrew Janda',
    'Danny G',
    'Will Evans',
    'Gannon Rice',
    'William Stevens',
    'Yunlin Zhang',
    'Colin Mackenzie',
    'Andrew',
    'Max Kushner',
    'Matthew Pearce',
    'Yiyuan Z',
    'DBationo (db)',
    'Secret Marina Permenter',
    'Jacob Aldridge',
    'Andrew Liu',
    'Ziang Chen',
    'Tobias Bautista',
    'Maria Paula Armenta',
    'Erik Ohst',
    'Ivan Yezhov (иван ежов)',
    'Cheng Xin',
    'kunming',
    'Lareina Gu',
    'Shadwa Eldosuky'
]

excelNames = [*set(excelNamesUnfiltered)
                ]  # only unique values from excel names

splitNames = []

def find_greater(a, b):
    if (len(a) > len(b)):
        return a
    else:
        return b

def find_smaller(a, b):
    if (len(a) > len(b)):
        return b
    else:
        return a

KeyValues = {"Matches": {}, "Partial Matches": {}}

def matchArgs(arg1, arg2):
    if ((arg2 in arg1) or (arg1 in arg2)):
        return True

def find_matches(index):
    rfirst = []
    rlast = []

    for i in range(0, len(splitNames)):

        for j in gNames["last"]:

            if (matchArgs(gNames["first"][j].lower(),
                            splitNames[i].lower()) == True):

                rfirst.append(j)

            if (matchArgs(gNames["last"][j].lower(),
                            splitNames[i].lower()) == True):

                rlast.append(j)

    return rfirst, rlast

for index in range(0, len(excelNames)):
    splitNames = excelNames[index].split()
    listFirst, listLast = find_matches(index)
    smallerList = find_smaller(listFirst, listLast)
    greaterList = find_greater(listFirst, listLast)

    for number in greaterList:
        if (number in smallerList):
            if (index in KeyValues["Matches"].keys()):
                KeyValues["Matches"][index].append(number)
            else:

                KeyValues["Matches"][index] = [number]

        elif (index in KeyValues["Partial Matches"].keys()):
            KeyValues["Partial Matches"][index].append(number)
        else:

            KeyValues["Partial Matches"][index] = [number]

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
                excelNames[i]
            ])
            final_list.append(indexofarray)

    """
    Add values to the partial match table. Adds the ID, First Name, Last Name and Excel Names
    """

    for i in KeyValues["Partial Matches"]:
        for indexofarray in [*set(KeyValues["Partial Matches"][i])]:
            p.add_row([
                indexofarray, gNames["first"][indexofarray], gNames["last"][indexofarray],
                excelNames[i]
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

show_results()
dup_list = final_list.copy()
# MVP working for deleting names
row_count = len(x.rows)

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


