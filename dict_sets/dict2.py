'''
a={23,25}

a.clear()
a.add(3)
a.remove(3)
a.update('dsdsdsds', 'fgfg')
a.difference(a)
a.discard('she') #discard ne vydaet oshybok
a.intersection(a)
a.intersection_update(a)
a.pop()


print(a)
'''
b={
	'sick': 12345,
	'flow': 43234}
a1={'lol': 'lololololo'}

#b.clear()
c=b.keys()
items=b.items()
d=b.values()
b.update(a1)

print(b,'\n',c, '\n',d) 
print(items)
print('Number1: ', b.get('sick'))



