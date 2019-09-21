#Coupon generator using list
import random

No_Rand_numbers = int(input("Enter the number of distinct random numbers needed: "))

list_0 = []

for i in range(0,No_Rand_numbers):
    
    Rand_number = random.randint(0,pow(2,30))
    #print(Rand_number)
    
    if(Rand_number in list_0):
        break
    else:
        list_0.append(Rand_number)
            
print(sorted(list_0))