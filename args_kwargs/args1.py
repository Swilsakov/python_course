        #1

# def add(num1, num2):    
#     print(num1 + num2) 
# add(num1 = eval(input('Введите 1 число: ')), num2 = eval(input('Введите 2 число: ')))


# def substract(num1, num2):
#     print(num1 + num2)
# substract(num1 = eval(input('Введите число номер 1:')), num2 = eval(input('Введите число номер 2:')))


# def multiply(num1, num2):
#     print(num1 * num2)
# multiply(num1 = eval(input('Введите число номер 1:')), num2 = eval(input('Введите число номер 2:')))


# def divide(num1, num2):
#     print(num1 / num2)
# divide(num1 = eval(input('Введите число номер 1:')), num2 = eval(input('Введите число номер 2:')))

# #Почти правильно но не то
# def divide():
#     print(num1 / num2)
# num1 = eval(input('Число номер 1:'))
# num2 = eval(input('Число номер 2:'))
# divide()


        #2
        #2.1 считает вместе с пробелами

# def word_sum(a):
#     c = 0
#     for x in a:
#         if ('a' <= x <= 'z') or ('A' <= x <= 'Z') or ('а' <= x <= 'я') or ('А' <= x <= 'Я'):
#             c += 1
#         else:
#             pass
#     print(c)
# a = input('Введите предложение:')
# word_sum(a)

        #2.2 считает без пробелов

# def func(str1):
#     ind = 0
#     for i in str1:
#         ind +=1
#     print(ind)
# str1 = input('Введите предложение:\n')
# func(str1)

        #3

# def dict(a, b):
#     a.update(b)
#     print(a)
# a = {'name': 'bob'}
# b = {'age': '12'}
# dict(a, b)

        #4

# def menu():
#     a = open('menu.txt', 'w')
#     menuFood = input('Что вы хотите заказать поесть?\n')
#     menuDrink = input('Что вы хотите заказать выпить?\n')
#     a.write(menuFood)
#     a.write(menuDrink)
#     a.write('')
#     a.close()
# menu()

        #5  
	#создание папки с определенным названием

# import os
# def word():
# 	word1 = str(input('Назовите свою директорию: '))
# 	filee = open(word1, 'a+')
# 	filee.close()
# word()
