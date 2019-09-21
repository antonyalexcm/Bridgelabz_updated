def anagram(string):
    dic = {}
    for i in string:
        d = list(str(i))
        d = sorted(d)
        dic[i] = d
    return dic
        


def Prime_Number(Num):
    list_1 = []
    for i in range(1, Num):
        flag = 0
        if(i == 1):
            pass
        else:
            for j in range(2,i):
                
                if(i%j == 0):
                    flag =  1
            if(flag == 0):
                list_1.append(i)
    
    return list_1
                                    
num = int(input("Enter the range upto which to check prime number:"))
lis = Prime_Number(num)

print("The prime numbers which are Palindromes are: ")
for i in lis:
    n=i
    new = 0 
    while(n>0):
        rem = n%10
        new = new*10 + rem
        n = (n//10)
        
    if new == i:
        pass
       # print(i)
#print("The numbers which are Anagrams are: ")


print('The prime numbers which are anagrams of each other are: ')

dikki = anagram(lis)
#print(dikki)


rev_dict = {} 

for key, value in dikki.items(): 
    #print("".join(value))
    rev_dict.setdefault(int("".join(value)), set()).add(key)

#print(rev_dict)
    

for key in rev_dict:
    if len(rev_dict[key])>1:
        print(rev_dict[key])