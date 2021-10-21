#1

# class Cars:
#     def noting(self):
#         pass
# class Moto(Cars):
#     def mNoting(self, world):
#         print(world + '!')
# a = Moto()
# a.mNoting('Hello')

#2
    #родительский класс

# class Person:
#     name = 'Ivan'
#     age = 457
     
#     def __setr(self, name, age): # защищенный метод это (__)
#         self.name = name
#         self.age = age

# class Student(Person):
#     course = 2

# a = Student()
# a._Person__setr('Igor', 112)
# a.course = 1
# print(a.course)

#3
    #родительский класс


# class Factory:
#     def engine(self):
#         return 'Двигатель готов, Сэр!'
#     def bridge(self):
#         return 'Ходовая часть готова!'

# q = Factory()
# print(q.engine())
# print(q.bridge())

# class Toyota(Factory):
#     def weels(self):
#         return 'Колеса готовы!'
#     def window(self):
#         return 'Стекла чисты как у кота одно место!'

# w = Toyota()
# print(w.weels())
# print(w.window())

# x = [q.engine(), q.bridge(), w.weels(), w.window()]
# print(x)

#4
    #публичный атрибут

# class Phone:
#     number = '999-999-777'
#     def print_num(self):
#         print('Phone number is: '+ self.number)
# my_num = Phone()
# my_num.print_num()


#5
    #dir и его работа, и приватные атрибуты(объекты) и методы(название функции)

# class Phone:
#     username = 'Bob'
#     __number = '101-111-010' #приватный или же защищеный атрибут

#     def call(self):
#         print('Ring-Ring')
#     def __bubon(self): #приватный метод
#         print('Num on: '+ self.__number)

# myPhone = Phone()
# myPhone.call()
# myPhone._Phone__bubon()

# print(dir(myPhone))

#классы можно импортировать!!!