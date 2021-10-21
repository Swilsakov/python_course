#операционная система
import os

#текущая директория
print(os.getcwd())

#рандом
import random
a = random.randint(0, 100)#обязательно диапозон только с int()
print(a)

b = random.choice(['vova', 'baiel', 'ramil', 'beka'])#работает с str()
print(b)

print(random.randrange(100))#схож с randint, но есть маленькая разница, можно без диапозона

print(random.random())# рандом с плавающей точкой



#time
import time
a = time.localtime(time.time())
print(a)