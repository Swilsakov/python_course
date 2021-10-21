'''
def myFunc():
	pass
def my_Func():
	print(5+5)
#мы можем использовать много раз
my_Func()
my_Func()
my_Func()
my_Func()
my_Func()


'''
#вызов глобальных функций
def rrr():
	global test#используется только при тех случаях когда нам необходимо пользоваться этой функцией
	test = 0
	return test
rrr()#обязательтно указывать имя функции
print(test)




