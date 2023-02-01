# Could have used regex and avoided 90% of the stuff done here but YOLO

from prettytable import PrettyTable
from main import *


def main():

    x = PrettyTable()
    p = PrettyTable()
    
  
    
    p.field_names = [ "ID", "First Name", "Last Name", "⌛  Partial Match"]
    x.field_names = [
        "ID", "First Name", "Last Name", " ✅ Full Match"
    ]

    # Conducting a Literature Review 11/1/2022

    gNames = export_list(First_name, Last_name)

    # create list with excel names
    excelNamesUnfiltered = [
        'Abd Alrhman Bani Issa',
        'Abigail Erskine',
        'Alex Ozbolt',
        'Allegra Stahl',
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

    def show_matches():
        
        for i in KeyValues["Matches"]:
            for indexofarray in [*set(KeyValues["Matches"][i])]:
                x.add_row([
                    indexofarray, gNames["first"][indexofarray], gNames["last"][indexofarray],
                    excelNames[i]
                ])


        for i in KeyValues["Partial Matches"]:
            for indexofarray in [*set(KeyValues["Partial Matches"][i])]:
                p.add_row([
                    indexofarray, gNames["first"][indexofarray], gNames["last"][indexofarray],
                    excelNames[i]
                ])
            

    show_matches()

    def show_results():

        x.sortby = "ID"
        p.sortby = "ID"
        print(x.get_string())
        print(p.get_string())


        r = PrettyTable()
       
        r.field_names = ["🧮 Total perfect matches:",'{:0>2}'.format(len(x.rows)),"⌛Total partial matches:", '{:0>2}'.format(len(p.rows))]

        
        print(r.get_string())

    show_results()

    # MVP working for deleting names
    row_count = len(x.rows)

    def user_delete_prompt():
        userin = int(input("Enter row to delete "))
        while(userin < 0 or userin > row_count):
            print("Please enter a number from 0 to", row_count-1)
            userin = int(input("Enter row to delete "))
        return userin
    
    

    
    

        

    # x.del_row(int(userin))
    # print(x.get_string(sortby="Index")) # TODO add validation




if __name__ == "__main__":
    main()
