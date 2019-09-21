# Coupon Generator using python random function
import random

No_Rand_numbers = int(input("Enter the number of distinct random numbers needed: "))

Rand_number = random.sample(range(0,pow(2,30)), No_Rand_numbers)
    

print(sorted(Rand_number))
