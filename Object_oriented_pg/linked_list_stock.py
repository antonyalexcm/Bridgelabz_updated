class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.count = 0


    def add_to_list(self, new_data):


        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.count +=1
    
    def delete_node(self, key): 

        temp = self.head 

        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                self.count -=1

                return
  
        while(temp is not None): 
            if temp.data == key: 
                break 
            prev = temp 
            temp = temp.next 
  
        if(temp == None): 
            return 1
        self.count -= 1
        prev.next = temp.next
        temp = None

    def list_sorting(self):
        
        temp1 = self.head
        while(temp1 != None):
            temp = self.head
            while(temp.next!= None):
                if(temp.data > temp.next.data):
                    tempo = temp.data
                    temp.data = temp.next.data
                    temp.next.data = tempo
                temp = temp.next
            temp1 = temp1.next


        
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def return_list(self):
        temp = self.head
        final_list = []
        while(temp):
            final_list.append(temp.data)
            temp = temp.next
        return final_list
   
    def search(self, x): 
 
        current = self.head 
   
        while(current != None): 
            if(current.data == x): 
                return True # data found 
            current = current.next
          
        return False # Data Not found 

if __name__ == "__main__":
    llist = Linkedlist()
    llist.add_to_list(1)
    llist.add_to_list(2)
    llist.add_to_list(3)
    llist.add_to_list(4)
    llist.add_to_list(5)

    print("\n")
    llist.print_list()
    llist.list_sorting()
    print("\n")
    llist.print_list()