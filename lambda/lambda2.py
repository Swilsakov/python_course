    #1.1

# import random 
# def ok(x):
#     o = []
#     for z in x():
#         if z not in o:
#             o.append(z)
#     print(o)
#     print(len(o))

# @ok
# def ko():
#     a1 = []
#     for i in range(100):
#         b = random.randint(10, 50)
#         a1.append(b)
#     return a1

    #1.2
    #не работает с декоратором

# import random
# from random import randint
# def gen():
#     def gen1():
#         listt = []
#         i = 0
#         for i in range(100):
#             a = random.randint(10, 50)
#             listt.append(a)
#             i+=1
#         print(listt)
# gen()

    #1.3

# from random import *
# def randomyi():
#     a = []
#     i = 0
#     while i <100:
#       s = randrange(10,50)
#       a.append(s)
#       i += 1
#     print(a)

#     a = set(a)
#     a = list(a)
#     print(a)  
# randomyi()
    
    #2.1

# def avtorizatsiy(x):
#   login = input("Ведите логин : ")
#   password = input(" Ведите пороль: ")
#   x(login,password)
# @avtorizatsiy
# def regist(login,password):
#   k = 0
#   for i in login:
#     print(k+ord(i))
#     break
#   for i in password:
#     print(k+ord(i))
#     break

    #2.2
        #Моя схема работы

# def shifr(x):
#     login = input('Введите логин: ')
#     password = input('Введите пароль: ')
#     x(login, password)

# @shifr
# def shifr1(login, password):
#     shL = []
#     shP = []
#     i = 0
#     for i in login:
#         shL1 = (ord(i))
#         shL.append(shL1)
#         for i in shL:
#             print(i, end= '')
#     # print('Ваш шифрованный логин: ', shL)
#     for i in password:
#         shP1 = (ord(i))
#         shP.append(shP1)
#     print('Ваш шифрованный пароль: ', shP)

    #3

# def lambda_func():
#     a = [1745345, 98726, 439872634, 7312, 64872, 123687126, 9312, 4124, 231, 3123, 34, 3453]
#     i = 0
#     for i in a:
#         sett = (lambda a,b: (b*a))(1.185, i)
#         print(sett)
# lambda_func()

