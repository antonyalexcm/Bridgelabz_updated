import N14_prime_numbers
import N11_Primenum_2d_array

def prime_and_anagram_printing(prime_list, anagram_list):

    i = 0
    new_array_anagram = []  
    new_array_prime = []
    for j in range(0,1000,100):
        
        new_arrayp = []
        new_arraya = []

        for q in prime_list:
            if q in range(j, j+100):
                new_arrayp.append(q)
        
        for a in anagram_list:
            if a in range(j, j+100):
                new_arraya.append(a)

        new_array_anagram.append(new_arraya)
        new_array_prime.append(new_arrayp)  

     
        print("\n")
        print("The prime numbers in the range {} to {} is :".format(j,j+100))
        print(new_array_prime[i])
        print("\r")
        print("The anagram numbers in the range {} to {} is :".format(j,j+100))
        print(new_array_anagram[i])
        i +=1

    return


def range_prime_and_anagram_generation():#Function to generate prime number in a ranges of 100 starting from 0 to 1000
    ''' Function to return prime number in ranges '''

    
    prim_num = N14_prime_numbers.print_prime()
    anagram_list = list(N14_prime_numbers.check_anagrams(prim_num))
    prime_and_anagram_printing(prim_num, anagram_list)

    return


# Driver function
if __name__ == "__main__":
    range_prime_and_anagram_generation()
