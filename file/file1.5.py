#Создайте database.txt файл с несколькими логинами и паролями. Затем попросите пользователя войти или зарегистрироваться. Спросите его логин и пароль. Если такой логин уже есть скажите ему что логин уже существует и предложите авторизоваться спросив пароль. Если такого логина неоказалось среди уже существющих продолжайте регистрацию. Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.

while True:
	print('sign or reg:')
	a = input()
	#1 sign
	if a == 'sign':
		login = input('Enter login:\n')
		password = input('Enter password\n')
		r = open('/home/vladimir/pylessons/les8/database.txt', 'r')
		if login in r.read():
			print('This login is there`s')
			print('You can make a new login')
		else:
			print('')
			print()
		#else:
			r = open('/home/vladimir/pylessons/les8/database.txt', 'w')
			r.write('aaa')
		

	#2 reg
	elif a == 'reg':
		print('login')


'''
	#3 while
	else:
		while a!='sign' or a!='login:':
			a=input('sign or login:\n')
			if a == 'sign':
				print('sign')
				break

			elif a == 'login':
				print('login')
				break
'''
			







# filedb = open('database.txt', 'a+')
# file = open('users.txt', 'w')
# login = input('your login:\n')
# password = input('your password:\n')
# file.write(login)
# file.write(password)
# print(file)

#a = input('enter login:')
#b = input('enter password:')
