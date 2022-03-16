# 16 NESTING LUG'ATLAR ICHIDA LUG'ATLAR

# car0 ={
#        'model':'lasetti', 'rang': 'oq',
#        'yil': 2018, 'narx':13000,
#        'km': 50000, 'karobka' : 'avtomat'
#        }
# car1 = {
#         'model':'nexia 3', 'rang': 'qora',
#        'yil': 2015, 'narx':9000,
#        'km': 89000, 'karobka' : 'mexanika'
#        }
# car2={
#       'model':'gentra', 'rang': 'qizil',
#        'yil': 2019, 'narx':15000,
#        'km': 20000, 'karobka' : 'mexanika'
#        }


# car = car0
# print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}- yil, {car['narx']}$")
        
# car = car1
# print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}- yil, {car['narx']}$")
        
# car = car2
# print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}- yil, {car['narx']}$")
      
      
      
      # OSON USUL
      
# cars = [car0, car1, car2]
# for car in cars:
#           print(f"{car['model'].title()},\
#       {car['rang']} rang,\
#       {car['yil']}- yil, {car['narx']}$")
      
      
      
# print(cars[0]['model'])


# print(f"{cars[2]['rang'].title()}", \
#       f"{cars[2]['model']}")
        
        
# malibus = []
# for n in range(10):
#     new_car = {
#         'model': 'Malibu',\
#             'rang': None,
#             'yil': 2020,
#             'narx': None,
#             'km': 0,
#             'karobka': 'avto',
#             }
#     malibus.append(new_car)
#     for malibu in malibus[:3]:
#             malibu['rang'] = 'qizil'
#     for malibu in malibus[3:6]:
#                 malibu["rang"]='qora'
#     for malibu in malibus:
#             if malibu['karobka']=='avto':
#                 malibu['narx']= 40000       
#             else:
#                 malibu['narh']=35000
# for malibu in malibus:
#             print(malibu.values())
            
        
        
        

        
# LUG'AT ICHIDA RO'YXAT
# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css', 'js'],
#     'husan': ['php', 'sql'],
#     'hasan': ['python', 'php'],
#     'maryam': ['c++', 'c#'] 
#             }        
# for ism,tillar in dasturchilar.items():
#     print(f"\n{ism.title()}:", end=' ')
#     for til in tillar:
#         print(f"{til.upper() }", end=  ' ')
            
#         Ali: PYTHON C++ 
# Vali: HTML CSS JS 
# Husan: PHP SQL 
# Hasan: PYTHON PHP 
# Maryam: C++ C# 
        
        # LUG'AT ICHIDA LUG'AT
# hamkasblar = {
#     'ali' :{'familiya' :' valiyev',
#             'tyil' : 1995,
#             'malumot' : "oliy",
#             'tillar' : ['python', 'c++']},

# 'vali' :{'familiya' :' aliyev',
#             'tyil' : 2001,
#             'malumot' : "o'rta maxsus",
#             'tillar' : ['html', 'css']
#                 },
# 'hasan': {'familiya':'husanov',
#             'tyil' : 1999,
#             'malumot' : "maxsus",
#             'tillar' : ['python',' php']}
#  }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()},"
#           f"{info['tyil']} - yilda tug'ulgan.n"
#           f"Ma'lumoti:{info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#               print(til.upper())
          
          





