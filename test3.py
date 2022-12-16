# Task 1

# class Client:
#     def __init__(self, full_name, balance):
#         self.full_name = full_name
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def set_balance(self, new_balance):
#         self.__balance = new_balance
#
#     def del_balance(self):
#         del self.__balance
#         print("balance was deleted")
#
#
# client = Client("Vika", 100_000_000)
# print(client.get_balance())
# client.set_balance(0)
# print(client.get_balance())
# client.del_balance()
# print(client.get_balance())

# Task 2

class Auto:

    def __init__(self, brand, model, km, price):
        self.brand = brand
        self.model = model
        self.km = km
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def del_price(self):
        del self.__price
        print("price was deleted")

    my_property = property(get_price, set_price, del_price, "I'm the price property.")


car_1 = Auto("Audi", "Q5", 2000, 50000)
print(car_1.my_property)
car_1.my_property = 10000
print(car_1.my_property)
# print(car_1.my_property.__doc__)
del car_1.my_property
print(car_1.my_property)



