class Employe:
    def __init__(self, name, lastN, money):
        self.name = name
        self.lastN = lastN
        self.momney = money
        self.email = name +'_'+ lastN + '@company.com'
    def full_name(self):
        return '{} {}'.format(self.name, self.lastN)        

emp_1 = Employe('Steve', 'Gold', '1,000$')
emp_2 = Employe('Max', 'Frost', '1,500$')

print(emp_1.email)
print(emp_2.name)

print(emp_1.full_name())