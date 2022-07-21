# -*- coding: utf-8 -*-
import datetime
import time
import inflect
p = inflect.engine()

# Function to get a number of input data from user.
def Get_Data():

    while True:
        print("How much data do you want to enter:")
        userInput = input()
        try:                                                      # Function only accept a interger value grater than 0 
            x = int(userInput)                                    # and rejects negative and other string input.
            if x > 0:
                break
            else:
                print("Please enter a valid number")
        except ValueError:
            print("Not a integer, try again")
    return x


# Function to get a date data from user. 
def Get_Day():
    date_format = '%d.%m.%Y'                                            
    while True:                                                         # Continuously ask for date data in valid formate if 
        print("Please enter a date (DD.MM.YYYY):")                      # invalid data or formate is provided.
        p = input()
        try:
            date_obj = datetime.datetime.strptime(p, date_format)
            break
        except ValueError:
            print("Incorrect date format, should be DD.MM.YYYY")
    return p


# Function to get a time data from user.
def Get_Time():
    time_format = '%H:%M'                                               
    while True:                                                         # Continuously ask for time data in valid formate if
        print("Please enter a time (HH:MM):")                           # invalid data or formate is provided.
        q = input()
        try:
            time_obj = datetime.datetime.strptime(q, time_format)
            break
        except ValueError:
            print("Incorrect time format, should be HH:MM")
    return q


        
# Main Function.        
def main():                                                      
    y = Get_Data()                                              # Function call to get a data from user.

    a = []                                                      # Empty list to store a time and date data from user.
    b = []
    i = 0

    while i < y:                                                # while loop to promote use to give a date and time data
        c = Get_Day()                                           # in case of one or more than one input.
        d = Get_Time()
        a.append(c+" - "+d)                                     # appends the date and respected time data in empty list.
        i += 1

    print("Thank you very much. I will notify them!")
    time.sleep(1)
    
    for z in range(0, len(a)):                                                                          # Loop to print a date and time data stored in list.
        b.append(z+1)
        print("The", p.number_to_words(p.ordinal(b[z])), "Date has been reached!", "(",a[z],")")
        
        
    
if __name__== "__main__":
    main()


