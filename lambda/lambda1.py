        #1.1
#куб

# a = eval(input('Введите длину куба: '))
# kub = (lambda a: (a*3))(a)
# print('Объем куба =', kub)

        #1.2

# kubik = (lambda a, b, c: (a*b*c))(5,7,4)
# print('Объем бассейна:', kubik)

        #2

# year = (lambda a, b: a-b) (365, 223)
# print('До нового года осталось:', year)

        #3.1
# def rec(a):
#     print(a)
#     if a % 2 == 0:
#         return a
#     else:
#         rec(a+2)

# rec(2)

        #3.2

# def rec(x):
#     print(x)
#     rec(x+2)
# rec(1) 

        #4

# def sett(a):
#     print(a)
#     if a == set():
#         return a
#     else:
#         a.pop()
#         return sett(a)
# d={'aaaa', '2df'}
# sett(d)
