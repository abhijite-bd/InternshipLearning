class Car:
    color = "black" 
    # @staticmethod
    def start(self):
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped.")
class ToyotaCar(Car):
    def __init__(self, name):
        self.name=name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("Marcdwdez")
print(car1.start())
Car.stop()  # Can be called on the class itself without creating an object.
print(Car.color)
