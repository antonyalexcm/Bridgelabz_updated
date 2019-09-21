lis = (input("Enter the numbers seperated by commas : "))
lis = [int(i) for i in lis.split(',')]
lis= sorted(lis)
print(lis)
d = int(input("Enter the element you have to find: "))
m=0
n = len(lis)
found = 0
for i in range(m,n):
    mid = int((m+n)/2)
    if(lis[mid] == d):
        print("The number is at index: " ,(mid))
        found = 1
        break
    elif(lis[mid] > d):
        n = mid
    elif(lis[mid] < d):
        m = mid
if(found == 0):
    print("Not Found!!!!")