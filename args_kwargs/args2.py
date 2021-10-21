        #1.1

# def first():
#     print('Я главная функшиорни')
#     second()
#     thirth()

# def second():
#     print('А я вложения функшиорни')

# def thirth():
#     print('А как же я, вы забыли про меня, я 3-я функшиорни')

# first()

        #1.2
# def fun():
#         print('main func')
#         def fun1():
#                 print('other func')
#         fun1()
# fun()
  
        #2

# def dic():
#     dik = {'color': 'red', 'fruit': 'banana'}
#     keys = (dik.keys())
#     values = (dik.values()) 
#     print(keys,'\n',values)
#     print(type(keys))
# dic()

        #3
	#алгоритм нахождения простых чисел

# def prostye_chisla():
# 	print('Алгоритм нахождения простых чисел')
# 	a = eval(input('Введите конечное число: '))
# 	for num in range(a):
# 		prime = True
# 		for i in range(2,num):
# 			if (num%i==0):
# 				prime = False
# 		if prime:
# 			print (num)
# prostye_chisla()