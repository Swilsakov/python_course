while True:
  w = input("Мы рады приветствовать вас на нашем сайте \n Выберите '1' чтобы Войти \n Выберите '2' что бы Зарегистрироватся : " )
  #Вход в систему
  if w == "1":
    file = open("database.txt" , "r") 
    f = (file.read().split())
    login = input("Введите Логин : \n")
    if login in f:
      password = input('Здраствуйте '+ login + '\nВведите пароль : ')
      if password in f:
        print("Вы успешно зашли в аккаунт")
      else:
        print('Неправильный пароль!!!')
    elif login not in f:
      print("Не удалось найти ваш логин!!!")
    file.close()
  #Регистрация в систему
  elif w == "2":
    file = open("database.txt" , "a+") 
    f = (file.read().split())
    login2 = input("Придумайте логин : \n")
    if login2 in f:
      print('Такой логин уже существует!!!')
    elif login2 not in f :
      file.write(login2)
      password2 = input("Придумайте пароль : ")
      password3 = input('Повторите пароль : ')   
      if password2 == password3:
        file.write(" ")
        file.write(password2)
        print("Поздравлем!!! \nВы успешно Зарегистрировались!!!")
      else: 
        print("Пароли не свопали!!!")
      file.close()
  else:
    print("Ошибка!!!")