import Stack_linked_list
import N14_prime_numbers

def linked_list_operation(liss):
    llist = Stack_linked_list.Stack()
    for i in liss:
        llist.push(i)
    return llist

def linked_list_removal(liss):
    num = int(input("Enter the number of elements that you want to remove : "))
    for i in range(0,num):
        liss.pop()
    return liss


#driver function
if __name__ =="__main__":
    #program to print prime numbers from 0 to 1000
    prim_num = N14_prime_numbers.print_prime()
    #checking whether the number is anagram or not
    dicti= N14_prime_numbers.check_anagrams(prim_num)
    list_anagrams = N14_prime_numbers.anagram_and_dictform(dicti)
    llist = linked_list_operation(list_anagrams)
    llist.display()
    print("\n")
    destacked_list = linked_list_removal(llist)
    print("\n Destacked list is : ")
    destacked_list.display()
    print("\n")