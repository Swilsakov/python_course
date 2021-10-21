    #recursia

        #1

# def main(number):
#     print(number)
#     if number == 0:
#         return number
#     else:
#         main(number+1)
# main(-20)

        #2

# def main(number):
#     print(number)
#     if number == 0:
#         return number
#     else:
#         main(number-1)
# main(10)

        #3
# def rec(x):
#     print(x)
#     rec(x+1)
# rec(1)      #можно менять значение, макс значение 995


        #4
# def rec(x):
#     if x < 10:
#         print(x)
#         rec(x+1)
#         print(x)
# rec(0)


        #5
# def rec(x):
#     if x < 10:
#         print(x)
#         rec(x+1)
# rec(1)


        #6
        #показывает максиманльое значение рекурсии

# import sys
# print(sys.getrecursionlimit())

        #7

# def itc(x):
#     if x <= 1:
#         return 1
#     else:
#         return x * itc(x-1)
# c = itc(eval(input('Enter number: ')))
# print(c)


     #lambda

        #1
#use without lambda

# def python(a, b):
#     print(a+b)
# python(10, 5)

#use lambda

# a = (lambda x, b: (x+b))(10,5)
# print(a)

    #decoratory

        #1

# @ - это декоратор

# def ok(x):
#     def nat():
#         print('start...')
#         x()
#         print('stop...')
#     return nat

# def ololo(c):
#     def kak():
#         print('start2...')
#         print('stop2...')
#         c()
#     return kak

# @ololo
# @ok
# def gg():
#     print('step...')
# gg()