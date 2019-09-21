limit = int(input("Enter the number: "))

if(limit<=31):
 for i in range(0,limit+1):
   print("2 ^ {} = {}".format(i,pow(2,i)))
else:
 print("\nRange exceeded!!")