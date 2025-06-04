# Task: Create a car class with attributes and display method 
class Car: #defining class 
    def __init__(self, make, model, year, color): #attributes
        # Initialize the car attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display(self): #display
        # Display the car details
        print("Car Details:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")


# Example usage
my_car = Car("Swift", "Desire", 2014, "Yellow")
my_car.display()