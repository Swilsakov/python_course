#1 =================================================================================================================

# class Student:
#     def __init__(self, name, lastname, department, year_of_entrance):
#         self.name = name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_entrance = year_of_entrance
#     def get_student_info(self):
#         print(self.name, self.lastname,', поступил в', self.year_of_entrance, 'году, в учебное заведение:', self.department)
# per = Student('Василий', 'Пупкин', 'Контора информационной безопасноти', '2576')
# per.get_student_info()

#2 ===========================================================================================================================

# class Airplane:
#     def __init__(self, make = ' Boing', model = '757', year = '2016', max_speed = '600 km/h', odometer = '10,000 m', is_flying = False):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = odometer
#         self.is_flying = is_flying
#     def take_off(self):
#         is_flying = True
#         land = False
#         print('Взлет')
#     def fly(self):
#         is_flying = True
#         land = False
#         print('Летит',self.max_speed, self.odometer)
#     def land(self):
#         is_flying = False
#         land = True
#         print('Приземление')

# a = Airplane()
# a.take_off()
# b = Airplane()
# b.fly()
# c = Airplane()
# c.land()

#3 ======================================================================================================================

# class Car:
#     def __init__(self, make, model, year, odometer=0, fuel=150):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel

#     def drive(self, distance):
#         fuel = distance / 10
#         if self.fuel >= fuel:
#             self.__add_distance(distance)
#             self.__subtract_fuel(fuel)
#             print('Let’s drive!')
#         else:
#             print('Need more fuel, please, fill more!')

#     def __add_distance(self, distance):
#         self.odometer += distance

#     def __subtract_fuel(self, fuel):
#         self.fuel -= fuel


# a = Car('sedan', 'avto', '2020')


# a._Car__add_distance(100)


# a._Car__subtract_fuel(100)


# print(a.drive(int('100')))

#4 ===================================================================================================

# 4) Список контактов
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [] на all_contacts =
# Список контактов(). Создайте несколько контактов, используйте метод
# search_by_name.


# class ContactList(list): #Создается дочерний клас Contact который унаследет от list
#     def search_by_name(self,*name): #Создан метод search_by_name который содержит в себе аргумент name 
#         self.sovpadenie = [] # Создается пустой листь для хранение совпадений
#         self.all_contacts = ["Bова","Канат","Жакып","Азат","Марат","Айдай",
#         "Умар","Динара","Султан","Жака","Асан","Нурмамат","НУрайым","Байэл"] #Создан лист из неких контактов
        
#         for i in name: #Создается цикл которое каждый раз проходится по name и передает его значения на i 
#             if i in self.all_contacts: #Создается условие: если заначение i есть внутри списка all_contacts
#                 self.sovpadenie.append(i) #то его добавляет в список sovpadenie
#                 print(f"Совпал контакт {i}!") #Выводится значенеи котрый совпал

#             elif i not in self.all_contacts: #Создается еще одно условие: если значение i не окажется внутри списка sovpadenie 
#                 print(f"Совпадений {i} не найдено!")#то Выводится значение которое не совпало

#         print(f"Список всех совпадений {self.sovpadenie}")#В конце выподится список Совпавших имен      

# s = ContactList() #Обявляется переменное на класс
# s.search_by_name('Вова',"Асан","Тилек","Нурмамат","Байэл","Кубат","Айдай") # Вызывыется метод с списком искомых имен


# 5 ====================================================================================================

# TASK 5  AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)

# import time#импорт времени в данной задаче необходима, чтобы имитировать время выстрела оружия

# class Soldier():#объявляем класс
#     def __init__(self, name, gun):# инициализируем значения
#         self.name = name #приравниваем
#         self.gun = gun #приравниваем

# class Guns():# объявляем еще один класс
#     def shoots(self):#указываем метод
#         print(f'{self.name} shoots from: {self.gun}')#выводим ззначения на экран (без переменных)
#         self.ammunition = 30# кол-во боеприпасов
#         while self.ammunition > 0:#начало цикла 
#             self.ammunition -= 1#30-1
#             print('tigi-tigitishh')#выводит значения на экран (имеено звук оружия)
#             time.sleep(0.3)#указываем с какой задержкой должно появляться на экране(указываем по желанию время)

#         if self.ammunition == 0:#если кол-во патронов будет равно 0 то в силу вступает следющий метод
#             self.reloads()#название метода который будет применим
#         else:
#             pass


#     def reloads(self):# название метода
#         self.reload = input('Do you want to reload weapon? y/n: ')#когда пули закончаться на экране будет предложена следующая опция перезарядки
#         if self.reload == 'y':# yes сокрашенно y означает да 
#             self.shoots()# запуск предыдущего метода т.е. продолжения стрельбы
#         else:
#             pass


# class Act_of_Shooting(Soldier, Guns):# дочерний класс т.е. происходит наследование от двух главных классов
#     def init(self, name, gun):# инициализация
#         Soldier.init(self, name, gun)# иницализация Soldier


# soldier1 = Act_of_Shooting('Soldier Ryan', 'AK47')# объявляем переменные для вывода на экран
# soldier1.shoots()#вызываем метод

#6 ============================================================================================================


# Мебель:


# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.



# class House():
#     def __init__(self, typehouse, areahouse): 
#         self.typehouse = typehouse
#         self.areahouse = areahouse

#     def get_house(self):
#         self.totalarea = 0
#         self.furnitures = {
#             'Кравать' : 4,
#             'Гардироб' : 2,
#             'Стол' : 1.5
#         }
#         for value in self.furnitures.values():
#             self.totalarea += value
#         print('Тип дома: ',self.typehouse," -- Общая площадь:",self.areahouse, "\n",list(self.furnitures.keys()),"\n" "Оставшаяся площадь: " ,self.areahouse - self.totalarea) 
# b = House('Квартира', 80)
# b.get_house()


#7 =========================================================================================================

# class Student: 
#   def __init__(self,name,lastname,age,objects): 
#     self.name = name
#     self.lastname = lastname
#     self.age = age
#     self.objects = objects
#   def disp(self):
#     print(self.name, self.lastname, self.age, self.objects)

# Steve = Student("Steven",'Shultz' , 23, "English")
# Johny = Student("Jonathan","Rosenberg", 24 , "Biology")
# Penny = Student("Penelope","Meramveliotakis", 21 , "Physics")
# Steve.disp()
# Johny.disp()
# Penny.disp()



#8 ===================================================================

# 1 past

# class MoneyFmt:
# 	def __init__(self, value = 0.0):
# 		self.value = float(value)
# 	def update(self, value = None):
# 		self.value = value
# 	def __str__(self):
# 		if self.value >= 0:
# 			return '${:,.2f}'.format(self.value)
# 		else:
# 			return '-${:,.2f}'.format(-self.value)
# 	def __repr__(self):
# 		print(self.value)
# 		return f'{self.value}'

# cash = MoneyFmt()

# 2 past


# from AlphaMoney import MoneyFmt
# def dollarize():

# 	cash = MoneyFmt(12345678.021)
# 	repr(cash)
# 	print(cash)
# 	cash.update(100000.4567)
# 	repr(cash)
# 	print(cash)
# 	cash.update(-0.3)
# 	repr(cash)
# 	print(cash)
# 	a1 = eval(input('Введите число и я переведу его в доллоровое значение: '))
# 	cash.update(a1)
# 	print(cash)

# 	a2 = input("Если хотите повторить процедуру введите '1' , для выхода введите Enter: ")
# 	while a2 == '1':
# 		a3 = eval(input('Введите число: \n'))
# 		cash.update(a3)
# 		print(cash)
# dollarize()



# 15 ======================================================================================


# import random


# class Card():
#     def __init__(self):
#         self.list = ['Червы', 'Бубны', 'Треф', 'Пики']
#         self.cards = []
#         self.cart = []
#         for card_num in range(0, 52):
#             r = str(card_num % 13)
#             if r == '0':
#                 r = 'K'
#             if r == '1':
#                 r = 'A'
#             if r == '12':
#                 r = 'Q'
#             if r == '11':
#                 r = 'J'
#             index = int((card_num / 13) % 13)
#             self.cards.append((r, self.list[index]))

#     def draw(self):
#         next = self.cards.pop(random.randint(0, len(self.cards) - 1))
#         return next

#     def deck(self):
#         c = Card()
#         for i in range(0, 52):
#             self.cart.append(c.draw())

#         print(self.cart[:])

# c = Card()
# c.deck()

#16 ===========================================================================================================

# from random import *
# from time import *
# class unit:
#     def __init__(self,n,team):
#         self.n = n
#         self.team = team

# class hero(unit):
#     def __init__(self,name,n,team,level = 0):
#         self.name= name
#         self.level = level
#         self.team=team
#     def level_up(self, s): 
#         self.level+=s


# Manas = hero("Манас",3914,"red")
# Bakai = hero("Бакай",5536,"blue")

# red_team = []
# blue_team = []

# voiny = int(input("Введите количество воинов: "))
# if voiny % 2 ==0:
#     voiny +=1
# for i in range(1,voiny+1):
#     d = choice([True,False])
#     if d == True:
#         red_team.append("Воин Манаса c номером "+str(i))
        
#     else:
#         blue_team.append("Воин Бакая c номером " +str(i))
# r,b=len(red_team),len(blue_team)

# if r > b: 
#     Manas.level_up(r//3)
#     Bakai.level_up(b//5)
# elif r < b:
#     Bakai.level_up(b//3)
#     Manas.level_up(r//5)


# print("\nВ войске героя",Manas.name+"а"+",",str(Manas.level)+"-го уровня,",r,"воинов!")
# for x in red_team:
#     print(x)
#     sleep(0.2)

# print("\n"+"В войске героя",Bakai.name+"а"+",",str(Bakai.level)+"-го уровня,",b,"воинов!")
# for x in blue_team:
#     print(x)
#     sleep(0.2)

# print("\n ****НАЧАЛСЯ БОЙ МЕЖДУ ВОИНАМИ МАНАСА И БАКАЯ*** ")
# sleep(1)
# if r > b:
#     g = 0
#     for i  in blue_team:
#         print(i,"умирает из рук",red_team[g],"и умерает сам" )
#         sleep(0.2)
#         b -=1
#         r -=1
#         g+=1
#     print(f"\nВ Бою одержал победу Герой {Manas.name} {Manas.level}-го уровня, У него Осталось ",r,"воинов!")         
# if r < b:
#     g = 0
#     for i  in red_team:
#         print(i,"умирает из рук",blue_team[g],"и умерает сам" )
#         sleep(0.2)
        
#         r -=1
#         g+=1
#     print(f"\nВ Бою одержал победу Герой {Bakai.name} {Bakai.level}-го уровня, У него Осталось ",b,"воинов!")