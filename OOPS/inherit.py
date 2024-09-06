class car:
   
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(car):
    def __init__(self, brand):
        self.brand = brand

class Fortunar(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortunar("diesel")
car2 = ToyotaCar("prius")

print(car1.start())
 

# # multiple inheritance
# class A:
#     var1 = "Welcome to class A"

# class B:
#     var2 = "welcome to class B"

# class C(A, B):
#     var3 = "welcome to class C"

# c1 = C()

# print(c1.var1)
# print(c1.var2)
# print(c1.var3)