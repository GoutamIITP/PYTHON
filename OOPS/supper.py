class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print('Car Started')

    @staticmethod
    def stop():
        print("Car Stopped.")

class fortunar(Car):
    def __init__(self, name, type):
        self.name = name 
        super().__init__(type)
        super().start()

car1 = fortunar("tata", "Electric")
print(car1.type)