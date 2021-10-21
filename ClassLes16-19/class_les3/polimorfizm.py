    #полиморфизм
    #полиморфизм служит для перезаписования метода или переопределение метода

# class Animal:
#     def voice(self):
#         print('Идет звук')

# class Dog(Animal):
#     def voice(self):
#         print('Woof, Woof')

# class Cat(Animal):
#     def voice(self):
#         print('Myao, Myao')

# a = Animal()
# cat1 = Cat()
# dog1 = Dog()
# farm = [a, cat1, dog1]
# for i in(farm):
#     i.voice()

#-------------------------------------------

# class Country:
#     def capital(self):
#         print('Capital: ')
#     def language(self):
#         print('Language: ')

# class USA(Country):
#     def capital(self):
#         print('Washington')
#     def language(self):
#         print('English')

# class Italy(Country):
#     def capital(self):
#         print('Milan')
#     def language(self):
#         print('Italian')

# obj_usa = USA()
# obj_it = Italy()
# obj_country = Country()
# for i in(obj_country, obj_usa, obj_it):
#     i.language()
#     i.capital()

#----------------------------------------------------------

# class Galaxy:
#     def typee(self):
#         pass
#     def stars(self):
#         pass

# class MilkyWay(Galaxy):
#     def name(self):
#         print('MilkyWay')
#     def typee(self):
#         print('Spiral')
#     def stars(self):
#         print('400 billion')

# class AndromedaGalaxy(Galaxy):
#     def name(self):
#         print('AndromedaGalaxy')
#     def typee(self):
#         print('Spiral')
#     def stars(self):
#         print('1 trillion')

# milky = MilkyWay()
# andr = AndromedaGalaxy()
# for i in(milky, andr):
#     i.name()
#     i.typee()
#     i.stars() 

#----------------------------------------------------------------

#  У меня есть класс с названием Person
class Person:
    #Я хочу чтобы он добавлял некие атрибуты в данном случае это имя
    def init(self, name):   
        # и вызываю атрибут (экземпляр класса)
        self.name = name

# создаю Метод и добавляю запись
    def talk(self):             
        return 'Lets go'
# Тут я создаю дочерний класс и назывю Америка
class American(Person):
    # И беру метод точно такой же как и в родительском и  это уже называется Полиморфизмом
    def talk(self):
        # И даю ему запись
        return 'Hello, Do you speak English?'
#Создаю класс и наследуюсь от Родительского класса
class Russian(Person):
    # И вызываю тот же метод одноименный и это есть полиморфизм когда я называю определенный метод и перезаписываю его как хоччу
    def talk(self):
        # И идет запись
        return 'Привет, а ты говоришь по русский?'

# тут я поленился давать несколько переменных и использую одну которая будет принимать значение моего атрибута
tourists = [American('Martin'), Russian('Григорий')]
# Тут я прописываю цикл который пройдется по каждому указанному классу и выведет
for tourist in tourists:
    # name + talk  Тоесть условие которое я задаю
    print(tourist.name + ':  ' + tourist.talk())