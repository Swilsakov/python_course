spisok_1 = 'Lamborgini 17 4456 2020 Paris USA 11 23'
numbers=[]
letters=[]
for i in spisok_1:
	if i.isnumeric():
		numbers.append(int(i))
	else:
		letters.append(i)
		print(numbers, '\n', letters)

'''for numbers in spisok_1:
	print(numbers, end=' ')
for letters in spisok_1:
	print(letters, end=' ')
'''
# num=spisok_1.sorted(int(numbers))
# let=spisok_1.(str(letters))
# print(numbers)