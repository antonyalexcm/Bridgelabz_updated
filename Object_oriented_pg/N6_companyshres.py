from datetime import datetime
import linked_list_stock


class Share:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.time_transact = time_transation()
       


def time_transation():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

class StockAccount:
    def __init__(self):
        self.value = 0
        self.company_shares_list = linked_list_stock.Linkedlist()
        self.stock_list = []

    def add_shares(self,name,number):
        new_share = Share(name,number)
        self.company_shares_list.add_to_list(new_share)
        self.stock_list.append(new_share)

    def buy(self,new_name,new_number):
        flag = False
        for i in self.stock_list:
            if(new_name == i.name):
                self.company_shares_list.delete_node(i)
                i.number += new_number
                flag = True
                i.time_transact = time_transation()
                self.company_shares_list.add_to_list(i)

        if(flag == False):
            new_share = Share(new_name,new_number)
            new_share.time_transact = time_transation()
            self.stock_list.append(new_share)
            self.company_shares_list.add_to_list(new_share)
            

    def sell(self,sell_name,sell_number):
        flag = False
        for i in self.stock_list:
            if(sell_name == i.name):
                self.company_shares_list.delete_node(i)
                i.number -= sell_number
                i.time_transact = time_transation()
                self.company_shares_list.add_to_list(i)
                if(i.number == 0):
                    self.stock_list.remove(i)
                    self.company_shares_list.delete_node(i)
                flag = True
        if(flag == False):
            print("\rNo such share available for sale!!!")
    def print_report(self):
        for i in self.stock_list:
            print("\nWe have {} shares of {} bought at {}".format(i.number,i.name,i.time_transact))
   
    def save_file(self):
        file_object = open("./Inventory_data_final.txt", 'w')
        for i in self.stock_list:
            data = str("\nWe have {} shares of {} bought at {}".format(i.number,i.name,i.time_transact))
            file_object.write(data)


def main():
    jpm = StockAccount()
    jpm.add_shares("fb",20)
    jpm.add_shares("apple",120)
    jpm.add_shares("msft",10)    
    jpm.add_shares("amzn",100)
    jpm.print_report()
   

#driver function
if __name__ =="__main__":
    main()

