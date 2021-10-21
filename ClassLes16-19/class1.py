        #problem 1.1

# class Laptop:
#     def __init__(self, model_name):
#         self.model = model_name
#         self.kharakteristics = []
#         self.processor()
#         self.ram()
#         self.video_card()
#         self.HDD()
#         self.display_size()

#     def processor(self):
#         self.kharakteristics.append('Intel® Core™ i5-10210U CPU @ 1.60GHz × 8 ')

#     def ram(self):
#         self.kharakteristics.append('8 Гб DDR4')

#     def video_card(self):
#         self.kharakteristics.append('Intel UHD Graphics')

#     def HDD(self):
#         self.kharakteristics.append('SSD 256 Гб')
    
#     def display_size(self):
#         self.kharakteristics.append('15,6 FHD')
    
# laptop = Laptop(model_name='Lenovo')
# print(laptop.model)
# print(laptop.kharakteristics)


        #problem 1.2

# class Lenovo:
#     def __init__(self, Процессор, Оперативная_Память, Видеокарта, Жёсткий_Диск, Размер_экрана):
#         self.Процессор = Процессор
#         self.Оперативная_Память = Оперативная_Память
#         self.Видеокарта = Видеокарта
#         self.Жёсткий_Диск = Жёсткий_Диск
#         self.Размер_экрана = Размер_экрана
       
#     def get_Lenovo_info(self):
#         print({'Процессор': self.Процессор, 'Оперативная Память': self.Оперативная_Память, 'Видеокарта': self.Видеокарта, 'Жёсткий Диск': self.Жёсткий_Диск, 'Размер_экрана': self.Размер_экрана})

# s = Lenovo('Intel® Core™ i5-10210U CPU @ 1.60GHz × 8 ', '8 Гб DDR4' , 'Mesa Intel® UHD Graphics (CML GT2)', 'SSD 256,1 GB', '15.6')
# s.get_Lenovo_info() 


		#problem 2
# colors = {
#     "black": {
#     "category": "hue",
#     "type": "primary",
#     "code": {
#     "rgba": [255,255,255,1],
#     "hex": "#000"
#     }
#     },
#     "white": {
#     "category": "value",
#     "code": {
#     "rgba": [0,0,0,1],
#     "hex": "#FFF"
#     }
#     },
#     "red": {
#     "category": "hue",
#     "type": "primary",
#     "code": {
#     "rgba": [255,0,0,1],
#     "hex": "#FF0"
#     }
#     },
#     "blue": {
#     "category": "hue",
#     "type": "primary",
#     "code": {
#     "rgba": [0,0,255,1],
#     "hex": "#00F"
#     }
#     },
#     "yellow": {
#     "category": "hue",
#     "type": "primary",
#     "code": {
#     "rgba": [255,255,0,1],
#     "hex": "#FF0"
#     }
#     },
#     "green": {
#     "category": "hue",
#     "type": "secondary",
#     "code": {
#     "rgba": [0,255,0,1],
#     "hex": "#0F0"
#     }
#     }
#     }
# class Deckt:
#     def __init__(self ,colors ):
#         self.colors = colors

#     def get_keys_tuple(self):
#         s = colors.keys()
#         t = tuple(s)
#         return t
#     def get_values_tuple(self):
#         r = colors.values()
#         t = tuple(r)
#         return t

#     def get_keys_list(self):
#         s = colors.keys()
#         t = list(s)
#         return t
#     def get_values_list(self):
#         r = colors.values()
#         t = list(r)
#         return t

#     def get_keys_set(self):
#         s = colors.keys()
#         t = set(s)
#         return t
#     def get_values_set(self):
#         r = colors.values()
#         t = set(r)
#         return t


# d = Deckt(colors)
# print(d.get_keys_tuple())
# print(d.get_values_tuple())
# print(d.get_keys_list())
# print(d.get_values_list())
# print(d.get_keys_set())
# print(d.get_values_set())