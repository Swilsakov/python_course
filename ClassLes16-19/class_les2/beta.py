#наследование

# class Animal:
#     def ana(self):
#         print('Идет звук')

# class Cat(Animal):
#     def pop(self):
#         print('Myaooo')

# class Dog(Animal):
#     def gaa(self):
#         print('Woof')

# a = Cat()
# a.ana()
# a.pop()

# b = Dog()
# b.ana()
# b.gaa()

    #без инициализации
# class Usa:
#     def people(self):
#         print('Many different people life in USA')

# class Men(Usa):
#     def man(self):
#         print('Men are great!')

# class Women(Usa):
#     def woman(self):
#         print('Men are better then women!')

# m = Men()
# m.people()
# m.man()

# w = Women()
# w.people()
# w.woman()

    #с инициализацией
# class Language:
  
#     def __init__(self, name, age, py='Python is grean language', java='Java is also great language', c='But C is better!'):
#         # здесь нельзя добавлять операторы(аргументы) тк это ошибка, и он не может вывести за границу переменную без self
#         self.py = py
#         self.java = java
#         self.c = c
#         self.name = name
#         self.age = age
#     def display(self):
#         print('Your name is', self.name, 'and', self.age, 'years old')

# lang = Language('12')
# lang.display()
# print(lang.py,',', lang.java,',', lang.c)



    #наглядный пример создания личности
# class Person:
#     def __init__(self, name, age, cash, home):
#         self.name = name
#         self.age = age
#         self.cash = cash
#         self.home = home
#     def do(self):
#         print(self.name, self.age, self.cash, self.home)
#     def money(self):
#         print(int(self.cash + 1000000))
# m = Person('Bob', '54', 100000000, 'Home in Germany')
# m.do()
# m.money()