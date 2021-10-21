
file = open('file.txt')
print(file.read())

file = open('file.txt', 'r')
file.readlines()
print(file)

file = open ('file.txt', 'w')
file.write('hello world\n')
file.write('python\n')
file.write('dsdsdsdd\n')
#file.close() #rabotaet kak princip posle OPEN

print(file)

file = open('file.txt', 'a+')
file.write('azat')
print(file)

with open('file.txt', 'r+') as file:
	file.write('itc')
