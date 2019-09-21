# Permutation using Recursion
def permute(s):
   if len(s) == 1:
     return s

   perm_list = [] # resulting list
   for a in s:
     remaining_elements = [x for x in s if x != a]
     #print(remaining_elements)
     z = permute(remaining_elements) # permutations of sublist
    
    
     for t in z: 
       perm_list.append(a + t)

   return perm_list


d = list(input("Enter the String :"))
q = permute(d)
print(q)