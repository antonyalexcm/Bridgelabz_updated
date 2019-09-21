#import sys
class Utility:
    
    def beg_week_of_month(month_find, year_find):
        d = int(1)
        m = int(month_find)
        y = int(year_find)
        try:
            if ((m in range(1,13)) and (y > 0 ) ):
    
                y0 = y - ((14 - m)/12)
                x = y0 + (y0/4) - (y0/100) + (y0/400)
                m0 = m + 12*((14-m)/12)-2
                d0 = (d + x + ((31*m0)/ 12))%7
                d0 = int(d0)
                

                return d0
        except:
            print("Error in the month or year !!!!")
    
    def leap_year_find(year):

        if(year in range(1000,10000)):
            if(year%400 == 0):
                return True
            elif((year%4 == 0) and (year%100 !=0)):
                return True
            else:
                return False


    def month_days(month, year):
        
        mon = month
    
        if(mon == 2):
            is_leap = Utility.leap_year_find(year)
            if(is_leap):
                return 29
            else:
                return 28
        elif month in [1,3,5,7,8,10,12]:
            return 31
        else:
            return 30


if __name__ == "__main__":

    rem = Utility.beg_week_of_month(11,2019)
    print(rem)

