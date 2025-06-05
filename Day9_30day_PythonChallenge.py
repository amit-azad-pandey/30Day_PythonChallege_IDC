class Car:
    def __init__(self,brand,model,year,mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
       

    def display(self):
        print(f"{self.brand} {self.model} launched {self.year} mileage of {self.mileage}km/L.\n")
    def start(self):
        print(f"The {self.model}'s engine is starting")
    
class ElecCar(Car):
    def __init__(self, brand, model, year, range):
        super().__init__(brand, model, year, mileage=0) 
        self.range = range
    
    def display(self):
        print(f"This is {self.brand} {self.model} launched in {self.year} with a range of {self.range}Km/KwH.\n{self.model} is an electric car")


c = Car("Maruti Suzuki","Brezza","2020",16)
c.display()
c.start()

e = ElecCar("Tata","Nexon Hybrid","2024",500)
e.display()
e.start()