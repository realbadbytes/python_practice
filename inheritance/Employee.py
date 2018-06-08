from Person import *

class Employee(Person):

    def __init__(self, first, last, age, staffnum):
        super(Employee, self).__init__(first, last, age)
        self.staffnumber = staffnum

    def __str__(self):
        return super(Employee, self).__str__() + ', ' + self.staffnumber


