def BubbleSort(arr):

    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                k = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = k
    return arr

arra = input("Enter the array : ")
arra = [ str(i) for i in arra.split(',')]
bub = BubbleSort(arra)
print("Sorted array : ", bub)