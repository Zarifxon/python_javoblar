# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
# email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida
#  qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin.
#  Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)


# def mijoz(ism, familiya, t_yil, t_joyi, email, tel_raqam):
#     mijoz1 = {'ism': ism,
#               'familiya': familiya,
#               't_yil': t_yil,
#               't_joyi' : t_joyi,
#               'email': email,
#               'tel_raqam':tel_raqam    
#               }
#     return mijoz1
# print("Mijozning ma'lumotlarini shakllantiramiz")
# mijozlar = []
# while True:
#     print("\n Quyidagi malumotlarni kiriting:", end = ' ' )
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     t_yil = input("Tug'ulgan yilingizni kiriting: ")
#     t_joyi = input("Tug'ulgan joyingizni kiiriting: ")
#     email = input("Emailingizni kiriting; ")
#     tel_raqam = input("Telefon raqamingizni kiriting: ")
#     mijozlar.append(mijoz(ism, familiya, t_yil, t_joyi, email, tel_raqam))
#     javob = input("Yana ro'yxat shakllantirasizmi? (yes\ no): ")
#     if javob == 'no':
#         break

# print(mijozlar)


# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, 
# va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar 
# haqidagi ma'lumotni konsolga chiqaring.


# def mijoz(ism, familiya, t_yil, t_joyi, email, tel_raqam):
#     mijoz1 = {'ism': ism,
#               'familiya': familiya,
#               't_yil': t_yil,
#               't_joyi' : t_joyi,
#               'email': email,
#               'tel_raqam':tel_raqam    
#               }
#     return mijoz1
# print("Mijozning ma'lumotlarini shakllantiramiz")
# mijozlar = []
# while True:
#     print("\n Quyidagi malumotlarni kiriting:", end = ' ' )
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     t_yil = input("Tug'ulgan yilingizni kiriting: ")
#     t_joyi = input("Tug'ulgan joyingizni kiiriting: ")
#     email = input("Emailingizni kiriting; ")
#     tel_raqam = input("Telefon raqamingizni kiriting: ")
#     mijozlar.append(mijoz(ism, familiya, t_yil, t_joyi, email, tel_raqam))
#     javob = input("Yana ro'yxat shakllantirasizmi? (yes\ no): ")
#     if javob == 'no':
#         break

# print(mijozlar)

# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing


# def uchta(x, y, z):
#     max =x
#     if y >= max:
#      max =y
#     if z>=max:
#      max = z

#     return max
   

# Foydalanuvchidan aylaning radiusini qabul qilib olib,
#  uning radiusini, diametrini, perimetri va yuzini lug'at 
#  ko'rinishida qaytaruvchi funksiya yozing

# def aylana_info(radius, pi = 3.14):
#     aylana = { 
#         'uzunligi': 2*pi*radius,
#         'yuza': pi*radius**2,
#         'diametr': 2*radius
#                 }
#     return aylana
   
    
   # Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing
   # (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi,
   #  1 dan katta musbat sonlar)


# def tub_sonlar_top(min,max):
#   tub_sonlar = [] 
#   for n in range(min, max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif (n==2):
#             tub = True
#         else:
#               for x in range(2,n):
#                   if(n%x==0):
#                       tub = False    
#         if tub:
#             tub_sonlar.append(n)
  # return tub_sonlar                     
          
# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi
#  sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi
#  ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi.
#  Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...



# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar


# print(fibonacci(10))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]




