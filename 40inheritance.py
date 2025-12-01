#base class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f"Name is {self.name} and age is {self.age}")

#derived class

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def get_info(self):
        super().get_info()
        print(f"Grade is {self.grade}")

S1 = Student("Suna", 23, 94)
S1.get_info()