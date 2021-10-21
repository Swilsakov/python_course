# work with file

#1

# a = open('/home/vladimir/directories.txt', 'w+')
# a.write('''bin    dev   lib    libx32      mnt   root  snap      sys  var
# boot   etc   lib32  lost+found  opt   run   srv       tmp
# cdrom  home  lib64  media       proc  sbin  swapfile  usr ''')

# print(a)


#2

# user = open('/home/vladimir/pylessons/file/newAsistent/users.txt', 'w+')
# login = input('Придумайте логин: ')
# user.write(login)
# password = input('Придумайте пароль: ')
# user.write(password)
# print(user)

#3

# file = open('/home/vladimir/pylessons/file/newAsistent/text.txt', 'r+')
# f = file.read()
# if 'w' in f:
#     print('Да, в тексте есть "w"')
# else:
#     print('Нет, в тексте нет "w"')
# print()
# print(f)


#4

# file = open('/home/vladimir/pylessons/file/newAsistent/classroom#1.txt', 'r+')
# f = file.read().split()
# listFile = []
# for i in f:
#     if 't' in i:
#         listFile.append(i)
#     if 'T' in i:
#         listFile.append(i)
#     else:
#         pass
# print(listFile)


#5

