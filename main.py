import time
from selenium import webdriver
from attendance import make_final_list, lxt, final_list

    

def main():
    # Type list will be given to mark attendance
    result = make_final_list()
    print((result))
    print((final_list))
    
    
if __name__ == '__main__':
    main()  
