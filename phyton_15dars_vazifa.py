# AMALIYOT
# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
# 
# py = {
#       'print':'Konsolga chiqarish',
#       'title':"Faqat so'zning birinchi harfini katta qiladi",
#       'sort': "Alifbo tartibida joylaydi",
#       'if': "agar",
#       'input': "kiritish",  
#       'lower': "soz'ning barcha harfini kichik qiladi",
#       'append':"Ro'yxatga qo'shimcha element qo'shadi",
#       'del':"Ro'yxatdan elementni o'chiradi",
#       'len': "Ro'yxat uzunlinini aniqlaydi"
#       }

# for kalit, qiymat in sorted(py.items()):
#     print(f"{kalit.title()}-{qiymat}")
    
# Davlatlar va ularning poytaxtlari lug'atini tuzing. \
    # Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, \
    #     alifbo ketma-ketligida konsolga chiqaring.

# dav = {'uzb': 'toshkent', 'baa': 'dubai', 'rosiya': 'maskva', 'xitoy': 'tokio'}
# for kalit, qiymat in sorted(dav.items()):
#     # print(f"Kalit: {kalit}")
    # print(f"Qiymat: {qiymat}")


# Foydalanuvchidan istalgan davlatni kiritishni so'rang 
# va shu davlatning poytaxtini konsolga chiqaring. 
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
# "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

# dav = {'uzb': 'toshkent', 'baa': 'dubai', 'rosiya': 'maskva', 'xitoy': 'tokio'}
# dav2 = input("Istalgan davlatni kiririting:").lower()
# for kalit, qiymat in sorted(dav.items()):
#  capital = dav.get(dav2)
# if capital == None:
#      print("Kechirasiz bunday davlat ro'yxatda yo'q ")
# else:
#      print(f"{dav2.upper()}ning poytaxti {capital.title()} shahri!")
 
 
 

# Restoran menusi lug'atini tuzing 
# (kamida 10 ta taom-narh juftligini kiriting).
#  Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
#  Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
#  agar taom menuda bo'lsa narhini ko'rsating, aks holda 
#  "bizda bunday taom yo'q" degan xabarni chiqaring.


taomnoma = {'osh':10000,
            'shashlik':19000,
            'pitsa':60000,
            'somsa': 10000,
            'kabob': 400000,
            'tort':100000,
            'qazi':500000,
            'shurvo':15000,
            'sup':5000,
            'manti':8000
            }

print("3 ta taom buyurtma bering:")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1} - taom:").lower())

for buyurtma in buyurtmalar:
        if buyurtma in taomnoma:
            print(f"{buyurtma.title()} {taomnoma[buyurtma]} so'm")
else:
          print(f"Kechirasiz, bizda {buyurtma} yo'q")



# JAVOBLAR
# python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'}

# for key, value in sorted(python_words.items()):
#     print(f"{key.title()} - {value}")
# Boolean - Mantiqiy qiymat
# Float - O'nlik son
# For - Biror amalni qayta-qayta bajarish tsikli
# If - Shartlarni tekshirish operatori
# Integer - Butun son
# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar):
#     print(davlat.upper())

# print('\nDavlatlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())
# Dunyo davlatlari:
# AQSH
# ITALIYA
# MALAYZIYA
# O'ZBEKISTON
# QIRG'IZISTON
# QOZOG'ISTON
# ROSSIYA
# SINGAPUR
# TOJIKISTON

# Davlatlarning poytaxtlari
# Bishkek
# Dushanbe
# Kuala-Lumpur
# Moskva
# Nursulton
# Rim
# Sungapur
# Toshkent
# Washington D.C.

# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
# Qaysi davlatning poytaxtini bilishni istaysiz?:Rossiya
# ROSSIYAning poytaxti Moskva shahri
# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }

# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")
# 3 ta taom buyurtma bering.
# 1-taom:osh
# 2-taom:non
# 3-taom:norin
# Osh 20000 so'm
# Non 4000 so'm
# Kechirasiz, bizda norin yo'q.