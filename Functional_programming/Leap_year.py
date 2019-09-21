# Program to check if a year is Leap year
year = int(input("Enter the year: "))

if(year in range(1000,10000)):
 if(year%400 == 0):
    print("{} is a LEAP year".format(year))
 elif((year%4 == 0) and (year%100 !=0)):
    print("{} is a LEAP year".fromat(year))
 else:
    print("Not a LEAP year")