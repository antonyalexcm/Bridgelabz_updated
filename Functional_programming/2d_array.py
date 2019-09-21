#Print a 2D array in Python
M = int(input("Enter the number of rows:"))
N = int(input("Enter the number of columns:"))

arr = [[0 for l in range(N)] for o in range (M)]

for i in range(M):
    for j in range(N):
        arr[i][j] = input("Enter {} row {} element:".format(i+1,j+1))
 
print("\n")
for row in arr:
    print(row)