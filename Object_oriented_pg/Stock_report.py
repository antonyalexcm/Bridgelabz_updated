

class Share:
    def __init__(self,name,price,number):
        self.name = name
        self.price = price
        self.number = number
    

class Portfolio:
    def __init__(self):
        self.value = 0
        self.portfolio = []
    def enter_stock(self,name,price,number):
        new_stock = Share(name,price,number)
        self.portfolio.append(new_stock)

    def portfolio_details(self):
        for i in self.portfolio:
            print("\rThe price of {} is {} and the number is {} and the value is {}.".format(i.name,i.price, i.number,i.price*i.number))
    def portfolio_total(self):
        for i in self.portfolio:
            self.value += i.number*i.price
            
    
if __name__ == "__main__":
    portico = Portfolio()
    portico.enter_stock("Apple",25,120)
    portico.enter_stock("FB",15,100)
    portico.portfolio_details()
    portico.portfolio_total()
    print("Total portfolio value = ",portico.value)
