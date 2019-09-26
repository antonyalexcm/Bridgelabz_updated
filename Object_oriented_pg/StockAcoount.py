''' @author:Antony Alex
    @version:3.7
    @purpose: Maintain a stock account'''




from datetime import datetime

class Share:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.time_transact = time_transation()


def time_transation():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

class Portfolio:
    def __init__(self):
        self.value = 0
        self.portfolio = []
    def enter_stock(self,name,price,number):
        new_stock = Share(name,number)
        self.portfolio.append(new_stock)

    def portfolio_details(self):
        for i in self.portfolio:
            print("\rThe price of {} is {} and the number is {} and the value is {}.".format(i.name,i.price, i.number,i.price*i.number))
    def portfolio_total(self):
        for i in self.portfolio:
            self.value += i.number*i.price

class StockAccount:
    def __init__(self):
        self.value = 0
        self.company_shares_list = []
    def add_shares(self,name,number):
        new_share = Share(name,number)
        self.company_shares_list.append(new_share)
    # def company_shares_value(self):
    #     for i in self.company_shares_list:
    #         self.value += i.number*i.price
    def buy(self,new_name,new_number):
        flag = False
        for i in self.company_shares_list:
            if(new_name == i.name):
                i.number += new_number
                flag = True
                i.time_transact = time_transation()
        if(flag == False):
            new_share = Share(new_name,new_number)
            self.company_shares_list.append(new_share)
            i.time_transact = time_transation()
    def sell(self,sell_name,sell_number):
        flag = False
        for i in self.company_shares_list:
            if(sell_name == i.name):
                i.number -= sell_number
                i.time_transact = time_transation()
                if(i.number == 0):
                    self.company_shares_list.remove(i)
                flag = True
        if(flag == False):
            print("\rNo such share available for sale!!!")
    def print_report(self):
        for i in self.company_shares_list:
            print("\nWe have {} shares of {} bought at {}".format(i.number,i.name,i.time_transact))
   
    def save_file(self):
        file_object = open("./Inventory_data_final.txt", 'w')
        for i in self.company_shares_list:
            data = str("\nWe have {} shares of {} bought at {}".format(i.number,i.name,i.time_transact))
            file_object.write(data)


def main():
    jpm = StockAccount()
    jpm.add_shares("fb",20)
    jpm.add_shares("apple",120)
    jpm.add_shares("msft",10)    
    jpm.add_shares("amzn",100)
    jpm.print_report()
    jpm.save_file()
   

#driver function
if __name__ =="__main__":
    main()

