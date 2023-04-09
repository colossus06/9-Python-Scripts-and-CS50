import sys


class Employee:

    raise_amount= 1.04
    num_employee= 0

    def __init__(self, first, last, pay):
        self.first= first
        self.last=last
        self.pay=pay

        Employee.num_employee +=1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount=amount

    
Employee.set_raise_amount(10)

print(Employee.num_employee)
emp1= Employee("Elka", "Kimmon", 5000)

print(str(emp1))
print(emp1.fullname())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(emp1.__dict__)
print(Employee.num_employee)