# def num():
#     a = 12
#     b = 8
#     return a + b
# print(num())

# def sum():
#     b = 12 + 5
#     c = 20 + 5
#     return b, c
# print(sum())

# def my_func(name, age, agaga=12.222222):
#     print('Hello', name)
#     print('Your age', age)
#     print(agaga)
# my_func('Mario', 20)

# def func(first_name, last_name):
#     print('First_name =',first_name,'\nLast_name =', last_name)
#     print("Full name =", first_name +' '+ last_name)
# func('Bob', 'Gold')

# #*args - это картежи
# def itc(*args):
#     print(args)
# itc(120, 23, 444, 'ffff', ['ssss', 233])
# print(type(itc))

# def func(*a):
#     print(a)
# func(123, 23, 33, 22, 'ffff')

 
#         #**kwargs - dict(Словари)
# def team(**kwargs):
#     print(kwargs)
    
# team(name = 'Vova, Beka', team3 = 'Nuraiym', team4 = 'Aidar')

# # * - args, ** - kwargs

# def team(name, *sok):
#     print(f'Hello: {name}')
#     for i in sok:
#         print(i, end=' ')
# team('Vova', 100, 200, 300)


# def num(name, **kwargs):
#     print(f'name: {name}')
#     for name, phone in kwargs.items():
#         print(f'{name}: {phone}')
# num('Vova', phone = '+996999', team = 'Pytohn')