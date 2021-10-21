import sys
import random
#1
'''
print('Hi {}'.format(sys.argv[1]))
'''

#2
'''
a = input('Any:')
b = input('Any too:')
print()
'''

#3
'''
a = eval(input('Введите N-oe число:'))
i = 0
while i != a:
	print(i)
	i+=1
'''


#4		#Камень-Ножницы-Бумага
print('========================================================================')
print('Камень-Ножницы-Бумага:\n', '1 - камень\n', '2 - ножницы\n', '3 - бумага' )
player = eval(input('Ваш ответ:\n'))

#player
if player == 1:
	print('Вы выбрали - Камень')

if player == 2:
	print('Вы выбрали - Ножницы')

if player == 3:
	print('Вы выбрали - Бумагу')		


	#os
pk = random.randint(1,3)

if pk == 1:
	print('Компьютер выбрал - Камень')

if pk == 2:
	print('Компьютер выбрал - Ножницы')

if pk == 3:
	print('Компьютер выбрал - Бумагу')

	#reshenie
if player == 1 and pk == 1:
	print('Ничья')
if player == 1 and pk == 2:
	print('Вы выиграли')
if player == 1 and pk == 3:
	print('Вы проиграли')

if player == 2 and pk == 1:
	print('Вы проиграли')
if player == 2 and pk == 2:
	print('Ничья')
if player == 2 and pk == 3:
	print('Вы выиграли')

if player == 3 and pk == 1:
	print('Вы выиграли')
if player == 3 and pk == 2:
	print('Вы проиграли')
if player == 3 and pk == 3:
	print('Ничья')

