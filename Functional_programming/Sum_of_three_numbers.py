#Sum of three numbers add to zero
inpt = input("Enter the values to find the sum to zero : ")

a = [int(i) for i in inpt.split(',')]

n = len(a)
flag = False

for j in range(0,n-2):
    for k in range(j+1,n-1):
        for l in range(k+1,n):
            if(a[j]+a[k]+a[l] == 0):
                print(a[j],a[k],a[l])
                flag = True
                
if(flag == False):
    print("No such pairs")