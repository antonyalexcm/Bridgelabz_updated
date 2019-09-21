# Harmonic Number
num = int(input("Enter the number:"))
q=0
if(num>0):
 for i  in range(1,(num+1)):
    q += float(1/(i))
 print("The HARMONIC number is: {} ".format(q))
else:
 print("Error!!")