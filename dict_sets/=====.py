#sets
#0

# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# dates_of_birth.discard(7)
# print(dates_of_birth)

#1

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# a = farm_1.intersection(farm_2)
# print(a)

#2

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# b = farm_2.difference(farm_1)
# print(b)

#3

# s = {5, 65, 23, 'adsa', ('asdsd')}
# s.add(55555555)
# a = s.pop()
# print(s, a)


#===========================dict============================================

# 0

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh_parmak'] = 130
# menu['lagman'] = 135 #1
# l = {'lagman': 135} #2
# menu.update(l) #2
# menu.pop('borsh')
# print(menu)

#1

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']
# print(menu)

#2

# s1 = {'diffetence', 'add', 'remove', 'intersaction', 'clear', 'update', 'discard', 'intersection_update', 'pop'}
# s2 = {'clear','keys', 'get', 'values','items', 'update'}

# a = s1.intersection(s2)
# print(a)

#3

# dictt = {}
# for i in range(3):
#     a = input('Введите логин:')
#     b = input('Введите пароль:')
#     dictt[a] = b
# # a = input()
# # b= input()
# # dictt[a]= b
# print(dictt)

#4

# per = {'Bob': 'Teacher', 'John': 'Saller', 'Vova': 'Developer', 'Beka': 'ItPytohn', 'Sanya': 'Driver'}
# name = str(per.keys())
# work = str(per.values())
# print('Здраствуйте', name, 'Прекрасная профессия', work)


#5

# a = set()
# for i in range(10):
#     b = input('Введите много чисел:')
#     a.add(b)

# print(tuple(a))


#6 удаление дубликата

# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']

# a = set(south_american_countries)
# south_american_countries = a
# print(list(a))


#7
 
# suitcase = []
# print('Ваш чемодан может запихнуть любых 5 вещей')

# while len(suitcase) < 5:
#     a = input('Вещь: ')
#     suitcase.append(a)
# print('Вы передумали и убрали одну вещь')
# suitcase.pop()
# print(suitcase)

#8

farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
b = farm_1.intersection(farm_2)
a = set()
a.update(b)
print(a)