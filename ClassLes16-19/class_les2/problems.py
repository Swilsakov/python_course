# problem 1 =======================================================================

# class Factory:
#     def engine(self):
#         return 'Двигатель создан'

#     def bridge(self):
#         return 'Ходовая часть создана'

# a = Factory()
# print(a.engine())
# print(a.bridge())


# problem 2 ===========================================================================

# class Toyota(Factory):
#     def wheels(self):
#         return 'Колеса готовы'

#     def window(self):
#         return 'Стекла готовы'

# toyota = Toyota()
# print(toyota.wheels())
# print(toyota.window())
# t1 = toyota.wheels()
# t2 = toyota.window()

# lis = [t1, t2]
# print(lis)


# problem 3 ===================================================

# class Zoo:
#     def __init__(self, animal_1 = "Тигр", animal_2 = "Бегемот", animal_3 = "Жираф"):
#         self.animal_1 = animal_1
#         self.animal_2 = animal_2
#         self.animal_3 = animal_3

# z = Zoo()
# z.animal_1 = 'Лев'
# z.animal_4 = [z.animal_2, z.animal_3]
# z.animal_3 = 'Змея'

# print(z.animal_1, z.animal_2, z.animal_3, z.animal_4)



# dop problem 1 ========================================================================================

# class Student:
#     def __init__(self, name, lastname, department, year_of_entrance):
#         self.name = name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_entrance = year_of_entrance

#     def get_student_info(self):
#         return "{} {} поступил на {} в {} году". format(self.name, 
#         self.lastname, self.department, self.year_of_entrance)

# a = Student('Bob', 'Gold', 'Факультет программирования', '2018')
# print(a.get_student_info())


# dop problem 2 ===================================================================================

# class Airplane:
#     def __init__(self, make = 'Boing', model = '757', year = '2014', max_speed = 600, odometer = 0, is_flying = False):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = odometer
#         self.is_flying = is_flying

#     def take_off(self):
#         is_flying = True
#         land = False
#         print(f'{self.make} {self.model} {self.year} года взлетает!')
#     def fly(self):
#         odometer = self.odometer + 8000
#         print(f'{self.make} {self.model} набрал максимальную скорость {self.max_speed} км/ч, высота полета составляет {odometer} м!')
#     def land(self):
#         land = True
#         is_flying = False
#         print(f'{self.make} {self.model} {self.year} года приземлился!')

# airpln = Airplane()
# airpln.take_off()
# airpln.fly()
# airpln.land()

# dop problem 3 =================================================================================

# class Car:
#      def __init__(self, make, model, year, odometer=0, fuel=70):
#          self.make = make
#          self.model = model
#          self.year = year
#          self.odometer = odometer
#          self.fuel = fuel

#      def drive(self, distance):
#          fuel = distance / 10
#          if self.fuel >= fuel:
#              self.__add_distance(distance)
#              self.__subtract_fuel(fuel)
#              print('Let’s drive!')
#          else:
#              print('Need more fuel, please, fill more!')

#      def __add_distance(self, distance):
#         self.odometer += distance

#      def __subtract_fuel(self, fuel):
#         self.fuel -= fuel


# a = Car('sedan', 'avto', '2020')
# dist = eval(input('Дистанция маршрута: '))
# print(a.drive(dist))


# dop problem 4 ==================================================================================================
