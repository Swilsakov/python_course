# Инкапсуляция

# class Human: # класс
#     object=1 # статичный атрибут
    
#     def __init__(self, a1): # инкапсуляция
#         self.a1 = a1  # динамический атрибут

#     def run(self): # обычный метод
#         return 'RUN' 
    
#     def __sing(self): # приватный метод
#         return 'sing' 

#     def _eat(self): # защищеный метод 
#         return 'EAT'

# ===============================================================================================
# Абстракция

# class Human: # класс
#     name = 'No name' # статический атрибут
#     age = 1234 
#     money = 9999999 

#     def __init__(self): # инициализация
#         self.scream = 'AAAAAAAAAA' # атрибут для объекта
    
#     def sleep(self): # метод
#         return 'Zz Zz Zz' 

# ==================================================================================================
# НАСЛЕДОВАНИЕ

# class Rich:
#     money = 10000000000 # статические поля
#     age = 30
    
#     def earn_money(self): # метод обычный 
#         return self.money + 1 

# class Birtuugan(Rich): # наследование класса
#     pass

# ==================================================================================================
# ПОЛИМОРФИЗМ

# class GrantForKyrgyzstan:
#     money = 10000000000000 #статический атрибут

#     def give_money(self): # обычный метод
#         return 'money for pople'

# class Chinovnik(GrantForKyrgyzstan): # наследование класса
#     def give_money(self): # переопределние метода класса GrantForKyrgyzstan
#         return 'money for me' 

# ======================================================================================================
# Экземпляр класса

# class Animal: 
#     name = 'Kuba' # атрибут статичный

# kuba = Animal() # создание объекта
# kuba.name # вызов атрибута
# kuba.age = 10 # создание нового атрибута
# print(kuba.__dict__) # вывод значений в виде словаря(dict)