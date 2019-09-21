#@Author : Antony Alex
#Python_version : 3.7
#Simulation of Banking counter using Queue

from random import randint

class node:

    def __init__(self, data):
        self.data = data
        self.next = None

class queue:

    counter_balance = 10_00_000
    
    def __init__(self):
        self.front = None
        self.last = None
    

    def is_empty(self):
        '''Function to check if the queue is empty'''
        return self.front == None

    def enqueue(self,data):
        '''Function to add element to the rear of the queue'''
        temp = node(data)
        if(self.last == None):
            self.front = temp
            self.last = self.front
            return
        self.last.next = temp
        self.last = temp


    def dequeue(self):
        '''Function to remove element from the front of the queue'''
        if self.is_empty():
            return 
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.last = None
        return

    def account_action(self):
        '''Function to operate on the account'''
        action = int(input("\n Enter -> 1 for Cash deposit \n\t  2 for Cash withdrawal "))
        if (action == 1):
            print("The current account balance is : {}".format(self.front.data))
            deposit = float(input("Enter the amount to deposit :"))
            self.front.data += deposit  
            queue.counter_deposit(deposit)
            print("The new account balance is : {}".format(self.front.data)) 
            queue.counterbalance()
            self.repeat_transaction()
            return

        elif(action == 2):
            print("The current account balance is : {}".format(self.front.data))
            withdraw = float(input("Enter the amount to withdraw :"))
            if (withdraw <= self.front.data and withdraw >=0 ):
                self.front.data -= withdraw
                queue.counter_withdraw(withdraw)
            
            elif(withdraw <=0):
                print("\nWrong Input !!!!")
            else:
                print("\nInsufficient Balance !!!!")

            print("The new account balance is : {}".format(self.front.data))
            queue.counterbalance()
            self.repeat_transaction()
            
        else:
            print("Invalid Input !!!")
            self.account_action()

    def repeat_transaction(self):
        '''Function to carryout repeated account operations'''
        repeat = str(input("Do you want to carryout transaction again (Y/N) : "))
        if(repeat == "Y" or repeat == "y" ):
            self.account_action()
        elif(repeat == "N" or repeat == "n" ):
            self.dequeue()
            self.check_queue()
        else:
            print("Invalid Input!!!")
            self.repeat_transaction()
    

    @staticmethod       
    def account_balance():
        '''Static method to generate random number'''
        account_balance = randint(0,1_00_000)
        return account_balance

    def counterbalance():
        ''' Funtion to return counter balance to the terminal''' 
        return print("The counter balance is : {}".format(queue.counter_balance))
    
    @classmethod
    def counter_deposit(cls,deposit_cash):
        '''Class method to deposit cash into the account'''
        cls.counter_balance += deposit_cash
        return
    
    @classmethod
    def counter_withdraw(cls,withdraw_cash):
        '''Class method to withdraw cash from the account'''
        cls.counter_balance -= withdraw_cash
        return

    def check_queue(self):
        '''Method to check if anyone is in the queue'''
        any_que = str(input("\nIs there anyone in queue (Enter True/False): "))
        if(any_que == 'True'):
            bal_of_cust = queue.account_balance()
            self.enqueue(bal_of_cust)
            self.account_action()
        elif(any_que == 'False'):
            print("Counter transaction terminated.")
            return
        else:
            print("Wrong input!!")
            self.check_queue()
            
#Driver Function
if __name__ == "__main__":
    nee_q=queue()
    nee_q.check_queue()