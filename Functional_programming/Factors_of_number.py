# Using Brute Force
def PrimeNum(list_0):
  list_2 = []
  
  for k in list_0:
   for j in range(2,k):
     if(k%j == 0):
      break
   else:
    list_2.append(k)
  return list_2
  
    
num = int(input("Enter the number: "))
list_1=[]
for i in  range(2,num):
 if(num%i == 0):
  list_1.append(i)
PrimeNum(list_1)