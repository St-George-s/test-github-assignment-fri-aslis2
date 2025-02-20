brands = ["Giant", "Trek", "Cannondale"]
frame_size = [20, 22, 24]
model = ["Escape 2", "Marlin 5"]
type = ["Hybrid", "Mountain"]
price = [450.00, 370.00]
electric_assist = ["False", "False"]

class Bicycle:
    def __init__(self, brands, model, frame_size, type, price, electric_assist):
        self.brands = brands
        self.model = model
        self.frame_size = frame_size
        self.type = type
        self.price = price
        self.electric_assist = electric_assist

bike1 = Bicycle("Giant", "Escape 2", 20, "Hybrid", 450.00, False)
bicycles = [bike1, Bicycle("Trek", "Marlin 5", 22, "Mountain", 370.00, False)]

class Car:
    def __init__(self, colour, make, year, price):
        self.colour = colour 
        self.make = make
        self.year = year
        self.price = price 


myFirstCar = Car("Blue", "Audi", 2016, 20000)
print(myFirstCar.colour)
print(myFirstCar.make)
print(myFirstCar.year)
print(myFirstCar.price)

cars = [myFirstCar, Car("yellow", "renault", 2014, 10000)]

#mySecondCar = Car("yellow")
#print(mySecondCar.colour)

#pet food
class PetFood:
    def __init__(self, brand, animal, weight, price, stock):
        self.brand = brand
        self.animal = animal
        self.weight = weight
        self.price = price 
        self.stock = stock 


foods = [PetFood("Purina", "Cat", 1.5, 24.99, 10), PetFood("Pedigree", "Dog", 2.0, 20)]
