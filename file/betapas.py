while True:
	print('sign or reg:')
	a = input()

#1 sign
	if a == 'sign':
		r = open('/home/vladimir/pylessons/les8/database.txt', 'r')
		f = (r.read().split())
		login = input('Enter login:\n')
		password = input('Enter password:\n')
		if login in f:
			print('This login is there, u can register')
			login = input('Enter login:\n')
			password = input('Enter password:\n')
			password1 = input('Enter password again:\n')
			if password1 == password:
				print('Succes')
				r = open('/home/vladimir/pylessons/les8/database.txt', 'w')
				r.write(password)
				r.write(login)
				r.close()
			elif password1 != password:
				print('Password mismatch')
			else:
				print('Try it')
		else:
			print('isn`t')
			
		
#2 reg
	elif a == "reg":
		file = open("database.txt" , "a+")
		f = (file.read().split())
		login2 = input("Придумайте логин : \n")
		if login2 in f:
			print('Такой логин уже существует!!!')
		elif login2 not in f :
			file.write(login2)
			password2 = input("Придумайте пароль : ")
			password3 = input('Повторите пароль : ')   
			if password2 == password3:
				file.write(" ")
				file.write(password2)
				print("Поздравлем!!! \nВы успешно Зарегистрировались!!!")
		else:
			print("Пароли не свопали!!!")
			file.close()
	else:
		print("Ошибка!!!")


