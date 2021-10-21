#добавление в строку

#=====================while=====================================

# i = 0
# while i < 1:
#     print(i)
#     i += 1 #четные числа

# i = 0
# while i < 10:
#     if i == 4:
#         print(i)
#         break
    
#     if i == 3:
#         print(i)
#         continue

#     if i == 2:
#         pass
#     print(i)
#     i += 1


    

#=============================for==================================

# o = [1,2,3,4,5,6,7]
# for i in o:
#     print(44)
#==============================================================

#1

# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in range(6):
#     if languages[i] == lang1:
#         print('its')
#     else:
#         print('no')
    
#2

# a = 'php'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == a:
#         print(i)
#         break
#     print(i)

#3

# a = 7
# for i in range(5):
#     a *= a
#     print(a)


#4

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# a = 0
# for i in languages:
#     print(a, i)
#     a += 1


#5

# for i in range(-9, 10):
#     print(10-abs(i), end=' ')


#6

# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# a = 0
# for i in range(len(names)):
#     i1 = i%2 
#     if i1 == 0:
#         print(names[i])

#7

# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in range(len(names)):
#     i1 = i%2
#     if i1 != 0:
#         print(names[i])

#8

# a = eval(input('Введите число: '))
# i = a%2
# if a >= 100 and a <1000:
#     print('Это число трехзначное')
    
# if a >=0 and i == 0:
#     print('Это число положительное и четное')
    
# if a%31 == 0:
#     print('Число делится без остатка на 31')

# if a > 100 and a%17 == 0 or a > 150 and a==13**2:
#     print('Это число больше 100 и делится на 17 без остатка, или число больше 150 и равно 13^2')
#     print(a)
# else:
#     pass

#9
# print('Условие 1: ')
# for i in range(-100, 100):
#     if i % 13 == 0 and i % 2 == 0:
#         i = i**2
#         print(i, end=' ')
# print('\nУсловие 2: ')   
# for a in range(-100, 100, 7):
#     if a % 2 != 0:
#         print(a, end=' ')
