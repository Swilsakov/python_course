        #1

# def func(friut, number):
#     print(list(friut))
#     print(list(number))
    

# func(['Apple', ('AAAAAAPPPPLLLLE')], [13])

        #2
# def nechto():
#     a = input('Введите число: ')
#     b = int(a)
#     c = a * b
#     print(c)
#     d = len(a)
#     f = len(c)
#     itog = f / d
#     print('Всех чисел',a ,'в этом тексте составляет:' , itog)
# nechto()

        #3
# def cashmoney(name, cash = 5000):
#     a = input('Введите свою зарплату: ')
#     if a == '':
#         print(name, '-', cash )
#     else:
#         print(name, '-', a)
# cashmoney(name = input('Введите свое имя: '))

        #4
# from random import *
# def randomyi(namber):
#   	a = []
#   	i = 0
#   	while i < namber:
#   		s = randrange(0,1000)
#   		if s in a :
#   			continue
#   		a.append(s)
#   		i += 1
#   	print(a)
# randomyi(namber = int(input("Введите число: ")))