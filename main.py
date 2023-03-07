import time
from selenium import webdriver
from attendance import make_final_list, lxt, show_results, find_matches
from post_attendance import mark_attendance


def main():
    # Type list will be given to mark attendance
    find_matches(0.79)
    show_results()
    result = make_final_list()
    table = lxt(result)
    
    # Print the final names that willy be marked
    print(table[0])
    # Print the total number of attendees
    print(table[1])
    # # Print the initial list 
    # print(lxt(final_list)[0])
    mark_attendance(result)
    
    
    
    
    
    
if __name__ == '__main__':
    main()  
