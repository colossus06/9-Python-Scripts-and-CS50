

class Employee:
    def __init__(self, first,last):
        self.first= first
        self.last=last
        self.email= first+ "."+ last +"@duke,com"


    # creating methods
    def fullname(self):
        # code reusability
        return "{}'s last name is {}".format(self.first, self.last)

        

emp_1 = Employee("Haley", "Gun")

print(Employee.fullname(emp_1))

print(emp_1.fullname())

def get_name():
    return input("Enter a name: ")


print(get_name())