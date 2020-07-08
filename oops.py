class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            return self.name + ' ' + "plays tennis"
        elif self.occupation == "actor":
            return self.name + ' ' + "shoots film"

    def speaks(self):
        print(self.name, " says how are you?")

tom = Human("tom cruise", "actor")

print(tom.do_work())
tom.speaks()

########################################################
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def salary(self):
        return self.pay

    def email_id(self):
        return self.email

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.fullname())
print(emp_1.salary())
print(emp_1.email_id())



