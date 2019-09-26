class Person:
    # creating and initializing person
    def __init__(self):
        self.first_name = input("Enter the first name of the person : ")
        if not self.first_name.isalpha():
            raise ValueError
        self.last_name = input("Enter the last name of the person : ")
        if not self.last_name.isalpha():
            raise ValueError
        self.address = input("Enter the address of the person : ")
        self.city = input("Enter the city of the person : ")
        if self.city.isdigit():
            raise ValueError
        self.state = input("Enter the state of the person : ")
        if self.state.isdigit():
            raise ValueError
        self.zip = int(input("Enter the zip of the person : "))
        #if self.zip.isalpha():
            #raise ValueError
        self.phone_number = int(input("Enter the phone number of the person : "))
        #if self.phone_number.isalpha():
            #raise ValueError

class Addressbook:
    # creating and initializing an Addressbook
    def __init__(self):
        self.element_in_address_book = []

    def add_person(self): 
        self.element_in_address_book.append(Person())
        self.addressbook_operation()

    def delete_address(self):
        fname_del = str(input("Enter the first name,of the address to be deleted :"))
        sname_del = str(input("Enter the second name, of the address to be deleted : "))
        flag = True
        for person in self.element_in_address_book:
            if(person.first_name == fname_del and person.last_name == sname_del):
                self.element_in_address_book.remove(person)
                print("{}, successfully deleted".format(fname_del))
                flag = False
        if(flag == True):
            print("No such address exists!!!")
        self.addressbook_operation()

    def addressbook_operation(self):

        print('''\n\t     1 -> Add an address
             2 -> Edit an address
             3 -> Delete an address
             4 -> Print in mailing list
             5 -> Sort by name
             6 -> Sort by ZIP
             7 -> Exit''')

        operation = int(input("\nEnter operation :"))

        if(operation == 1):
            self.add_person()
        elif(operation == 2):
            self.edit_address()
        elif(operation == 3):
            self.delete_address()
        elif(operation == 4):
            self.print_in_mailing_list()
        elif(operation == 5):
            self.sort_by_name()
        elif(operation == 6):
            self.sort_by_zip()
        elif(operation == 7):
            pass
        else:
            print("\nWrong Selection, Try again!!")
            self.addressbook_operation()

    
    def edit_address(self):
        fname_edit = str(input("Enter the first name,of the address to be edited :"))
        sname_edit = str(input("Enter the second name, of the address to be edited : "))
        for person in self.element_in_address_book:
            if(person.first_name == fname_edit and person.last_name == sname_edit):
                print("\rPerson's first name and last name cannot be changed")
                person.address = str(input("Enter the new address of the person : "))
                person.city = str(input("Enter the new city of the person : "))
                person.state = str(input("Enter the new state of the person : "))
                person.zip = int(input("Enter the new zip code of the person : "))
                person.phone_number = int(input("Enter the new phone number of the person : "))
            else:
                print("No such address exists!!!")
        self.addressbook_operation()
    
    def print_in_mailing_list(self):
        details = int(input('''\n\t     1 -> Print entire address book in mailing list format
             2 -> Print a particular address from the book\n
             '''))

        if(details == 1):
            for person in self.element_in_address_book:
                print("\r{} {}".format(person.first_name,person.last_name))
                print("\r{}, {}".format(person.address,person.city))
                print("\r{}, {}".format(person.state,person.zip))
                print("\r{}".format(person.phone_number))
                print("\r")

        

        elif(details == 2):
            fname_print = str(input("Enter the first name,of the address to be printed :"))
            sname_print = str(input("Enter the second name, of the address to be printed : "))
        
            for person in self.element_in_address_book:
                if(person.first_name == fname_print and person.last_name == sname_print):
                        print("\r")
                        print("\r{} {}".format(person.first_name,person.last_name))
                        print("\r{}, {}".format(person.address,person.city))
                        print("\r{}, {}".format(person.state,person.zip))
                        print("\r{}".format(person.phone_number))

        self.addressbook_operation()

    def sort_by_name(self):
        self.element_in_address_book.sort(key = lambda x: (x.first_name, x.last_name))
        print("\r")
        for person in self.element_in_address_book:
                print("\r{} {}".format(person.first_name,person.last_name))
                print("\r{}, {}".format(person.address,person.city))
                print("\r{}, {}".format(person.state,person.zip))
                print("\r{}".format(person.phone_number))
                print("\r")
        self.addressbook_operation()
        
    
    def sort_by_zip(self):
        self.element_in_address_book.sort(key = lambda x: x.zip)
        print("\r")
        for person in self.element_in_address_book:
                print("\r{} {}".format(person.first_name,person.last_name))
                print("\r{}, {}".format(person.address,person.city))
                print("\r{}, {}".format(person.state,person.zip))
                print("\r{}".format(person.phone_number))
                print("\r")
        self.addressbook_operation()



def main():
    adressy = Addressbook()
    adressy.addressbook_operation()

if __name__ == "__main__":
    main()
