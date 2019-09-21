import sys
import Utility

def find_beg_day_ofmonth(month,year):
    week_day = Utility.Utility.beg_week_of_month(month, year)
    return week_day

def num_of_days(month, year):
    days_in_month = Utility.Utility.month_days(month,year)
    return days_in_month

def calendar_print(month, year,week_day, days_in_month):
    ''' Function to print the calendar '''
    print("\nPython cal", month,year)
    print("\r")
    
    number_of_days = days_in_month
    start_day = week_day
    day_lis = []
    print("S  M  T  W  Th  F  S") 
    print("\r")
    new_line = [6,13,20,27,34]
    for i in range(0,start_day):
        day_lis.append("  ")
    for k in range(1,number_of_days+1):
        day_lis.append(k)
    for index,j in enumerate(day_lis):
        if j == "  ":
            pass
        else:
            if (int(j)<10):
                print("",end = ' ')
        print(j,end = " ")
        if index in new_line:
            print("\r")
            print("  ")
        if (index == len(day_lis)-1):
            print("\n")

#Driver program
if __name__ =="__main__":
    
    month = int(sys.argv[1]) #getting the month and year values from th commandline
    year = int(sys.argv[2])
    week_day = find_beg_day_ofmonth(month, year)
    print(week_day)
    days_in_month = num_of_days(month, year)

    calendar_print(month, year,week_day, days_in_month)



    