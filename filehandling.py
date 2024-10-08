# Define the Car class
class Car:
    # Initializer method to define instance variables
    def __init__(self, make, model, year):
        self.make = make  # Instance variable for car make
        self.model = model  # Instance variable for car model
        self.year = year  # Instance variable for car year

    # Instance method to describe the car
    def description(self):
        return f"This car is a {self.year} {self.make} {self.model}."

# Create objects of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

# Accessing instance methods and variables
print(car1.description())  # Output: This car is a 2020 Toyota Corolla.
print(car2.description())  # Output: This car is a 2018 Honda Civic.

