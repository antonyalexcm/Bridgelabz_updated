import linked_list

def file_handling():

    """ Function to read the file to carry out the operations """
    #opens the file in read and write mode
    file_to_read = open("/home/admin1/Antony_Alex/Alex/Bridgelabz/data_structures/unordered_list/ListReading", "r+")  
    contents_in_file = file_to_read.read()
    file_to_read.close()
    print(contents_in_file)
    #Used to erase the contents of the file
    open("/home/admin1/Antony_Alex/Alex/Bridgelabz/data_structures/unordered_list/ListReading", "w").close()
    #print(contents_in_file)
    list_of_numbers = contents_in_file.split()
    return list_of_numbers
       

def add_to_file(return_list):

    final_sentence = ' '.join(return_list)
    file_to_read = open("/home/admin1/Antony_Alex/Alex/Bridgelabz/data_structures/unordered_list/ListReading", "r+")
    file_to_read.write(final_sentence)
    file_to_read.close()
    return

def llist_addition(word_list):
 
    llist = linked_list.Linkedlist()      
    for i in word_list:
        llist.add_to_list(i)
    
    return llist

def word_to_find():
    word_needed = str(input("Enter the word to find or to insert : "))
    return word_needed
def main():
    #list_strings =  file_handling()
    word_list = file_handling()
    llist = llist_addition(word_list) 
    word_needed = str(input("Enter the word to find or to insert : "))
    find_word = llist.search(word_needed)

    if (find_word == True):
        llist.delete_node(word_needed)
    else:
        llist.add_to_list(word_needed)

    return_list = llist.return_list()
    return_list.reverse()
    add_to_file(return_list)

    final_file = open("/home/admin1/Antony_Alex/Alex/Bridgelabz/data_structures/unordered_list/ListReading", "r")
    print(final_file.read())
    final_file.close()



if __name__ == "__main__":
    main()

    
