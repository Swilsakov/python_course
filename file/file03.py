#Создайте программу, которая считает из файла текст, и если в тексте содержится 
#буква “w”, то выведет на экран “Да, в тексте есть w”, иначе - 
#“Нет, в тексте нет w”. Подсказка: используйте ключевое слово in.

#method 1
'''
file=open('name.txt', 'r')

for i in file:
	if 'w' in i:
		print('Yes, there is "w" in text')
	else:
		print('No, there isn`t "w" in text')
'''
#method 2
file=open('name.txt', 'r')
a=file.read()
for i in a:
	if 'w' in i:
		print('Yes, there is "w" in text')
	else:
		print('No, there isn`t "w" in text')
