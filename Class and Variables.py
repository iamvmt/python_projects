lass Employee:
    companyName = "Apple"
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"THe name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")


emp1 = Employee("Harry")
emp1.rasie_amount = 0.03
emp1.companyName = "Google"
emp1.showDetails()
emp2 = Employee("Rohan")
emp2.showDetails()
