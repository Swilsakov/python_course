		#1 деление по полам и переворот списка
'''
def half():
	list_1 = ['name', 'age', '1', '19']
	a = list_1[:2]
	b = list_1[2:]
	a.reverse()
	b.reverse()
	lists = a + b
	print(lists)
half()
#для простеньких задач

		#1.02
#a, b = b, a
def half2():
	list_1 = ['name', 'age', '1', '19']
	for i in range(len(list_1)):
		if i % 2 == 0:
			list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
	print(list_1)
half2()

		#1.03
def half3():
    a = input().split()
    print((list(reversed(a[:(int(len(a)) // 2)]))) 
    + (list(reversed(a[(int(len(a)) // 2)::]))))
half3()

'''

		#2 Число Фибоначи

# a = eval(input('Введите конечное число Фибонначи: '))
# a=4
# def fib(n):
# 	a, b = 0, 1
# 	for i in range(n):
# 		yield a
# 		a, b = b, a + b
# print(list(fib(a)))




		#3		
# def func1():
# 	a = 5 + 5
# 	print(a)
# def func2():
# 	b = 5 - 5
# 	print(b)
# def func3():
# 	func1()
# 	func2()
# func3()
