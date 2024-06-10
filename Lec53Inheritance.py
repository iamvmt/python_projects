#  When a class derives from another class. the child class will inherirt all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods, this is called as inheritance.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee having ID:{self.id} is {self.name}.")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python.")


e1 = Employee("VMT", 2022071079)
e1.showDetails()
e2 = Programmer("Avani", 2022071021)
e2.showDetails()
e2.showLanguage()
