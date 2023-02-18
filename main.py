import time
from selenium import webdriver
from attendance import make_final_list, lxt, final_list


def main():
    # Type list will be given to mark attendance
    result = make_final_list()
    table = lxt(result)
    
    # Print the final names that will be marked
    print(table[0])
    # Print the total number of attendees
    print(table[1])
    # Print the initial list 
    print(lxt(final_list)[0])
    
    
    
if __name__ == '__main__':
    main()  
