class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None 

class dequeue:

    def __init__(self):
        self.front = None
        self.last = None
        self.count = 0

    def add_front(self, data):
        new_nodef = Node(data)
        if(self.front == None):
            self.front = self.last = new_nodef
            self.count +=1
        else:
            new_nodef.next = self.front
            self.front.prev = new_nodef
            self.front = new_nodef
            self.count +=1

    
    def add_last(self,data):
        new_nodeb = Node(data)
        if(self.last == None):
            self.last = self.front = new_nodeb
            self.count +=1

        else:
            new_nodeb.prev = self.last
            self.last.next = new_nodeb
            self.last = new_nodeb 
            self.count +=1
    
    def print_list(self):
        if(self.front == None):
            return
        temp = self.front
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def remove_front(self):
        if(self.front == None):
            return
        else:
            self.front = self.front.next
            if(self.front == None):
                self.last  = None
                return
            self.count -= 1
            self.front.prev = None

    def remove_last(self):
        if(self.last == None):
            return
        else:
            self.last = self.last.prev
            if(self.last == None):
                self.front  = None
                return
            self.count -= 1    
            self.last.next = None
    
    def is_empty(self):
        if(self.count == 0):
            return True
        else: 
            return False
    def size(self):
        print(self.count)
    

    def entry(self):
         
        pal_to_check = str(input("Enter the string to check whether palindrome or not :"))
        pal_list = [str(i) for i in pal_to_check]
        print(pal_list)
        pal_check_con = llist.pal_check(pal_list)
        print("Is palindrome :",pal_check_con)
    
    def pal_check(self, pal_lis): 
        for i in pal_lis:
            llist.add_front(i)
        while(self.count != 0):
            if(self.front.data == self.last.data):
                llist.remove_front()
                if(self.count > 1):
                    llist.remove_last()                
            else:
                return False
            if(self.count == 1):
                break  
        return True


#Driver function
if __name__=="__main__":
    
    llist = dequeue()
    llist.entry()

