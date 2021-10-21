import random
import sys
import os


#1

# import my_module

#2

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# a = []

# for i in range(4):
#     n = random.choice(names)
#     a.append(n)

# print(a)

#3

# print(os.name)
# print(sys.platform)

#4

# a = input()
# print(a)
# while a != '':
#     a = input()
#     print(a)

#5.1

# path = '/home/vladimir/mmmm'
# try:
#     os.makedirs(path)
# except OSError:
#     print ("Создать директорию %s не удалось" % path)
# else:
#     print ("Успешно создана директория %s" % path)

# w = open('/home/vladimir/mmmm/a.txt', 'w+')
# w = open('/home/vladimir/mmmm/v.py', 'w+')
# w = open('/home/vladimir/mmmm/d.js', 'w+')
# w = open('/home/vladimir/mmmm/s.txt', 'w+')
# w = open('/home/vladimir/mmmm/se.py', 'w+')

#5.2

# import subprocess
# subprocess.call('mkdir /home/vladimir/NEWEWEWEWEWEW', shell = True)
# # subprocess.call('ls', shell = True)

#6

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# teams = [[], [], [], []]
# i = 0

# while i <= len(names):
#     a = random.choice(names)
#     t = random.randint(0, 3)
#     teams[t].append(a)
#     i += 1

# print(teams)


#=======================================================================================================================
#1

# a = input()
# sys.stderr.write(a)
# print(sys.argv)

#2

# a = input()
# b = input()
# a1 = (sys.getsizeof(a))
# b1 = (sys.getsizeof(b))
# if a1 > b1:
#     print(f'Первое значение {a1} больше чем второе')  
# elif b1 > a1:
#     print(f'Второе значение {b1} больше чем первое')

#3.1

# num = int(input('Введите сколько символов должно быть у пароля: '))

# pas = []
# for i in range(0, num):
#     r = random.randint(0,9)
#     pas.append(str(r))
# for i in pas:
#     print(i, end='')
# print()

#3.2
#Генерация паролей
# import random
# chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# number = input('количество паролей: ')
# length = input('длина пароля: ')
# number = int(number)
# length = int(length)
# for n in range(number):
#     password =''
#     for i in range(length):
#         password += random.choice(chars)
#     print(password)
#4

#============================================================================================
#2

# import random

# def get_number():
#     num = [1, 4, 5, 7, 9, 0]
#     a = []
#     for i in range(6):
#         b = random.choice(num)
#         a.append(b)
#     print(f'0444{a[0]}{a[1]}{a[2]}{a[3]}{a[4]}{a[5]}')
# get_number()
        