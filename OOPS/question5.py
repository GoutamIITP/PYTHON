'''Create a class called Order which stores item & its price
Use Dunder function __gt__() to convey that:
     order1 > order2 if price of order1 > price of order2'''


class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, od2):
        return self.price > od2.price


od1 = order("Chips", 20)
od2 = order("kurkare", 25)

print(od1  >  od2)