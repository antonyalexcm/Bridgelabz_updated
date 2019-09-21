def search(lo, hi):
    ''' Number Guessing function '''
    if((hi - lo) == 1):
        return lo

    mid = int((lo + hi)/2)
    
    d = input("Is the number less than {} (True/False) : ".format(mid))
    print(d)
    if(d in ["True", "T","1"]):
        return search(lo, mid)
    else:
        return search(mid, hi)


if __name__ == "__main__":
    #n = pow(2,36) \
    print(search.__doc__)
    print("Think of a number between {} and {} : ".format(0 , 50))
    p = search(0,50)
    print("The number is : ",p)
    