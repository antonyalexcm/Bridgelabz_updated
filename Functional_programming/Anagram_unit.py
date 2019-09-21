# Anagram Unit using Itertools
from itertools import permutations

val = str(input("Enter the first string : "))
val2 = str(input("Enter the second string : "))

d = list(permutations(val))
k = []
for i in d:
    i = "".join(i)
    k.append(i)
    

if val2 in k:
    print(val + " and " + val2 +" are anagrams.")
else:
    print(val + " and " + val2 + " are not anagrams .")
