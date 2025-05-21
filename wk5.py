# Base class representing a general vehicle
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print(f"{self.name} is moving at {self.speed} km/h.")

    def description(self):
        print(f"{self.name} is a vehicle that can move.")

# Subclass for Car
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road 🚗 at {self.speed} km/h.")

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the sky ✈️ at {self.speed} km/h.")

# Subclass for Bicycle
class Bicycle(Vehicle):
    def move(self):
        print(f"{self.name} is pedaling along the path 🚴 at {self.speed} km/h.")

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on the water 🚢 at {self.speed} km/h.")

# Function to demonstrate polymorphism
def travel(vehicle):
    vehicle.description()
    vehicle.move()

# Create different vehicle objects with unique values
car = Car("Honda Civic", 100)
plane = Plane("Airbus A320", 850)
bike = Bicycle("Mountain Bike", 25)
boat = Boat("Yacht", 55)

# Use the same function to trigger different behaviors
vehicles = [car, plane, bike, boat]

for v in vehicles:
    travel(v)
    print("-" * 40)

