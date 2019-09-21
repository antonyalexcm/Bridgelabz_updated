import linked_list

def file_handling():

    """ Function to read the file to carry out the operations """
    #pens the file in read and write mode

    file_to_read = open("/home/admin1/Antony_Alex/Alex/Bridgelabz/data_structures/unordered_list/number_reading", "r+")  
    contents_in_file = file_to_read.read()
    file_to_read.close()
    #Used to erase the contents of the file
    open("/home/admin1/Antony_Alex/Alex/Bridgelabz/data_structures/unordered_list/number_reading", "w").close()
    print(contents_in_file)
    list_of_words = contents_in_file.split()
    list_of_words =[int(i) for i in list_of_words]
    return list_of_words

def find_num():
    num_to_find = int(input("Enter the number to check : "))
    return num_to_find


def llist_addition(numb_list):
 
    llist = linked_list.Linkedlist()      
    for i in numb_list:
        llist.add_to_list(i)
    return llist

def operate_on_llist(num_needed,llist):
    find_num = llist.search(num_needed)
    if (find_num == True):
        llist.delete_node(num_needed)
    else:
        llist.add_to_list(num_needed)
        llist.list_sorting()
    return llist
        

def llist_operation(num_list):
    llist = llist_addition(num_list)
    llist.list_sorting()
    print("\r The sorted list is :")
    llist.print_list()
    num = find_num()
    llist = operate_on_llist(num,llist)
    llist.print_list()
    return_list = llist.return_list()
    return_list = [str(i) for i in return_list]

    add_to_file(return_list)

def add_to_file(return_list):
    
    final_sentence = ' '.join(return_list)
    print(final_sentence)
    file_to_read = open("/home/admin1/Antony_Alex/Alex/Bridgelabz/data_structures/unordered_list/number_reading", "r+")
    file_to_read.write(final_sentence)
    file_to_read.close()
    return




if __name__ =="__main__":

    num_list = file_handling()
    llist_operation(num_list)
    


