class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: ", self.__maxprice)

    def set_maxprice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.set_maxprice(1000)
c.sell()
