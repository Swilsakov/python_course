#1

		#1 вариант с переменной
'''
from my_module import a
print(a)
'''

		#2 вариант с принтом
'''
import my_module
print(my_module)
'''

#2
'''
from random import sample
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
print(sample(names,4))
'''

#3
'''
import sys
print(sys.platform)
'''
'''
import os
print(os.name)
'''

#4
		#1 вариант
'''
import sys

print("Привет {}. Добро пожаловать в руководство по {} на {}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

#python test.py Студенты sys PythonRu  это в терминал

		#2 вариант
'''


#5

'''
import os
import random
os.mkdir('Test1')
i=0
while i<5:
	o=random.randint(0, 10)
	os.mknod(f'/home/vladimir/pylessons/les10/Test1/1{o}.txt')
	i = i + 1
	print(i)
'''

#6
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]






'''
import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
i = 0
a1=[]
a2=[]
a3=[]
a4=[]
while i != names:
	q = random.choice(names)
	if q not in a1:
		a1.append(q)
		i+=1

i = 0
while i != names:
	q = random.choice(names)
	if q not in a2:
		a2.append(q)
		i+=1

i = 0
while i != names:
	q = random.choice(names)
	if q not in a3:
		a3.append(q)
		i+=1

i = 0
while i != names:
	q = random.choice(names)
	if q not in a4:
		a4.append(q)
		i+=1
'''
