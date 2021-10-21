		#1

# Classroom = []
# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00) 
# for i in values:
# 	try:
# 		set(i)
# 		Classroom.append(True)
# 	except TypeError:
# 		Classroom.append(False)
# print(all(Classroom))



		#2

# l = []
# print('Введите 5 чисел')
# for i in range(5):
# 	a = eval(input())
# 	l.append(a)
# print('Самое миниманльое число это:', min(l))


		#3

# try:
# 	i = input('Введите функцию Python: ')
# 	eval(i)	
# except:
# 	print('Что-то не так...')

		#4

# print('Добро пожаловать на наш оффициальный сайт PyBank')
# summ = eval(input('Сумма займа должна составлять не менее $ 50,000\nВведите сумму: $ '))
# while summ < 50000:
# 	print('========================================================================')
# 	print('Сумма должна составлять больше $50,000')
# 	a = eval(input('Введите сумму: $ '))
# 	if a > 50000:
# 		protsent1 = 3.47
# 		itog = a * (protsent1 / 100)
# 		print('Вам необходимо заплатить итоговую сумму процента (3.47%): $', round(itog, 2))
# 		break
# if summ >= 50000:		
# 	protsent = 3.47
# 	itog = summ * (protsent / 100)
# 	print('Вам необходимо заплатить итоговую сумму процента (3.47%): $', round(itog, 2))
