
customer = input("Catogery:")


class Customer:
    # globals customer
    # customer == 'vip'
    def __init__(self, amount):
        self.amount = 1000

    def diss(self):
        # global customer
        if customer == 'normal':
            return self.amount - (self.amount * 0.2)

# c = Customer(1000).diss()
# print(c)


class VipCustomer(Customer):

    # if customer == 'vip'
    def __init__(self, amount):
        # super().__init__(amount)
        self.amount = amount

    def discount(self):
        # global customer
        # super().diss()
        # super().__init__(amount)
        if customer == 'vip':
            return self.amount - (self.amount * 0.4)


v = VipCustomer(1000).discount()
print(v)
# print(v.diss())
# .diss()
# print(v)
# print(Customer(1000).diss())
