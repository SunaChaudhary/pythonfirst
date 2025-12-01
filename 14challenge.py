#parent class
class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def details(self):
        print(f"Name of vehile is {self.make} and model is {self.model}")

#derived class
class Car(Vehicle):
    def __init__(self, make,model,year):
        super().__init__(make,model)
        self.year = year
    def details(self):
        super().details()
        print(f"Year is {self.year}")

C1 = Car("Honda", "Civic", 1998)
C2 = Car("Toyota", "Camry",2005)

C1.details()
C2.details()