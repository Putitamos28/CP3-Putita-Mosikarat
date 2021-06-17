class Vehicle:
    licenseCode = ""
    serialCode = ""
    face =""
    def turnOnAirConditioner(self):
        print("Turn ob : Air")
class Car(Vehicle):
    def sayHello(self):
        print("Hello World")
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()
car2 = PickUp()
car2.turnOnAirConditioner()
car3 = Van()
car3.turnOnAirConditioner()
car4 = Estatecar()
car4.turnOnAirConditioner()
