try:
	a = 1/0
except ZeroDivisionError:
	print("Ошибка")
except: 
	print('Ошибка') # если ошибка в except
else:
	print('Правильно') # если все правильно в except 
finally:
	print('Любой')# Работает в любом случае