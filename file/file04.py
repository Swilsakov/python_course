#Создайте текстовый файл python.txt и запишите в него текст #1 из Classroom:
#Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит
#букву “t” или “T”, то запишите его в список t_words = [ ]. После окончания списка,
#выведите на экран все полученные слова. Подсказка: используйте for.


file = open('python.txt', 'r')
t_words = []
b = (file.read().split())
for i in b:
	if 't' in i:
		t_words.append(i)
	if 'T' in i:
		t_words.append(i)
print(t_words)
file.close()