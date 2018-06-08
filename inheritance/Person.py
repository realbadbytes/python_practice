class Person(object):

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + ' ' + self.lastname + ', ' + str(self.age)
