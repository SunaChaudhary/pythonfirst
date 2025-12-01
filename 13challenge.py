# class Laptop

class Laptop:
    def __init__(self, id, name, ram):
        self.id = id
        self.name = name
        self.ram = ram
    def details(self):
        return f"id is {self.id}, name is {self.name} and ram is {self.ram}"
    
#obejct
L1 = Laptop(12, "Dell", "16 GB")
L2 = Laptop(13, "HP", "4 GB")
L3 = Laptop(14, "Acer", "8 GB")

print(L1.details())
print(L2.details())
print(L3.details())