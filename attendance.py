# Could have used regex and avoided 90% of the stuff done here but YOLO

from prettytable import PrettyTable
from main import *


def main():

    x = PrettyTable()
    x.field_names = [
        "Index", "First Name", "Last Name", "⌛  Partial Match", " ✅ Full Match"
    ]

    # Conducting a Literature Review 11/1/2022

    gNames = export_list(First_name, Last_name)

    # create list with excel names
    excelNamesUnfiltered = [
        'Abd Alrhman Bani Issa', 'Abigail Erskine', 'Alex Ozbolt', 'Allegra Stahl',
        'Connor Lazzaro', 'Elvis Junior Dun-Dery', 'Enoch Tetteh Amoatey',
        'Enoch Tetteh Amoatey', 'Favour Ojike', 'Francisco', 'Francisco',
        'Hailey Arreola', 'Heather Howard', 'Ifunanya Ezekiel', 'Ifunanya Ezekiel',
        'Jak', 'Javid Mardanov', 'Jed Wang', 'JOSEPH ALI',
        'Kayla Pasteur (kayla pasteur)', 'mberikou',
        'Mofareh Alzahrani # Alzahrm@purdue.edu', 'Monica Agu', 'Monica Agu',
        'Nigar Karimli', 'Padde Musa', 'Padde Musa', 'Padde Musa', 'Rajan Mishra',
        'Rashi Jain', 'Ravishankar Chatta Subramaniam',
        'Ravishankar Chatta Subramaniam', 'Ravishankar Chatta Subramaniam',
        'Ravishankar Chatta Subramaniam', 'Ravishankar Chatta Subramaniam',
        'Ravishankar Chatta Subramaniam', 'Rishi', 'Samarnh Pang', 'Shuqi Liao',
        'Shuqi Liao', 'Trey Cluff', 'Uche Chidi', 'Uche Chidi (chidi’s iPa)',
        'Vishwa Chandupatla', 'William Murray Keller', 'Ying Cheng Chen',
        'Abbas Naseem'
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
        counter = 1
        for i in KeyValues["Matches"]:
            for indexofarray in [*set(KeyValues["Matches"][i])]:
                x.add_row([
                    counter, gNames["first"][indexofarray], gNames["last"][indexofarray], "-",
                    excelNames[i]
                ])
                counter = counter + 1

        for i in KeyValues["Partial Matches"]:
            for indexofarray in [*set(KeyValues["Partial Matches"][i])]:
                x.add_row([
                    counter, gNames["first"][indexofarray], gNames["last"][indexofarray],
                    excelNames[i], "-"
                ])
                counter = counter + 1

    show_matches()

    def show_results():

        x.sortby = "Last Name"
        print(x.get_string(sortby="Index"))

        # TODO Fix this : Showing stats for perfect and partial matches (does not work)
        print("-" * 60)
        print("|", "🧮 Total perfect matches:",
              '{:0>2}'.format(len(KeyValues["Matches"])), "|",
              "Total partial matches:",
              '{:0>2}'.format(len(KeyValues["Partial Matches"])), "|")
        print("-" * 60)
        # print('📃 KeyValues:', KeyValues)

    show_results()
    
    # MVP working for deleting names
    userin = input("Enter row to delete")
    x.del_row(int(userin)-1)
    print(x.get_string(sortby="Index"))
    


if __name__ == "__main__":
    main()
