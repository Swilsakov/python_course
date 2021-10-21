# b = {'sss', 'sdfe', 'asfer'}
# a = {1, 23, 6, 7}
# print(a, '\n', b, type(a))

# a = set('aaaassssffffdd')
# print(a)
# #spisok
# b = set([1,2,3,4,4,4,3,56])
# print(b)

# a = set(range(5))
# print(a)
# #dictionary(dict)
# a = {'itc': 'python', 'bootcamp': 'js'}#takje i chisla
# print(a, type(a))

# a=dict(python=1, java=2, c=3)#rabotaet tolko s (str kluch)
# print(a)

# a = dict.fromkeys(['python', 'js', 'C'], 100)#key ...=100
# print(a)
# #dict
# b={}
# a='python the best language'
# a=a.split()
# b['питон']=a[0]
# b['является ']=a[1]
# b['лучшим']=a[2]
# b['языком']=a[3]
# print(a)
# print(b)


# a = {1, 3, 5, 'Fff', ('dddd', 1)}
# a.pop()
# print(a)

# b = {44, 5443, 76, 'fdfdfdf'}
# c = {656, 44, 76, 'gfgfgd'}
# print(b.difference(c))
# print(b.intersection(c))


d = {'fff': 1, (12,31): True}
print(d)

#добавление ключа
d['faf'] = 'Values'
print(d)
print(d.keys())
print(d.values())
print(d.get((12,31)))#обращаться только к ключам

#конвертация
print(set(d))
print(list(d))
print(tuple(d))
print(str(d))
