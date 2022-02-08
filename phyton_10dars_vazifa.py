  # AMALIYOT
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# yangi_cars = ['tayota', 'mazda', 'hyundai','gm', 'kia']
# for cars in yangi_cars:
#     if cars =='gm':
#         print(cars.upper())
#     else:
#         print(cars.title())
        
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# yangi_cars = ['tayota', 'mazda', 'hyundai','gm', 'kia']
# for cars in yangi_cars:
#     if cars !='gm':
#         print(cars.upper())
#     else:
#         print(cars.title())
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.

# login = input('Ismizni kiriting:')
# if login == 'admin':

#     print("Xush kelibsiz,", login.upper(), "Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print("Xush kelibsiz,", login.title())
    
 # Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# x = int(input("Birinchi sonni kiriting:"))
# y = int(input("Ikkinchi sonni kiriting:"))
# if x==y:
#     print("Siz kiritgan sonlar bir - biriga teng!", x,y)
# else:
#     print("Siz kiritgan sonlar bir biriga o'xshamaydi")



# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.

# son = int(input("Sonni kiriting:"))
# if son >0:
#     print("Kiritgan soningiz Musbat!")
# else:
#     print("Kiritgan soningiz Manfiy!")

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
# son = int(input("Musbat son kiriting:"))
# if son>0:
#     ildiz = son**0.5
#     print(son, "ning ildizi", ildiz," ga teng")
# else:
#     print("Musbat son kiriting!")
    #KIRITILGAN SONNING JUFT YOKI TOQ SONLIGINI ANIQLOVCHI DASTUR TUZING
son = int(input('Sonni kiriting:'))
if son % 2 == 0:
     print("Bu son Juft son", son)
else:
     print("Bu son Toq son", son)
    




