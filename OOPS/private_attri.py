class person:
    __name = "anonymous"

    def __hello(self):
        print("Hello person")

    def welcome(self):
        self.__hello()

p1 = person()

# print(p1.__hello())
print(p1.welcome())