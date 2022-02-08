# AMALIYOT
# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
son = int(input("Faqat juft son kiriting:"))
if son % 2 ==0:
    print("Rahmat")
else:
    print("Bu son juft emas")
    

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("Yoshingizni kirting:"))    


# if yosh<=4 or yosh>=60:
#     narh = 0;
     
# elif yosh<18:
#     narh = 10000;
# else:
#     narh = 20000;   

# print(f"Sizga chipta {narh} - so'm")  



# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

# x = float(input("Birinchi sonni kiriting:"))
# y = float(input("Ikkinchi sonni kiriting:"))
# if x == y:
#   print(f"Bu sonlar bir biriga teng! x = {x}, y = {y}")
# elif x>y:
#   print("Bu sonlardan:", x, ">", y, "birinchi son katta ekan!")   
# else:
#       print("Bu sonlardan:", x, "<", y, "ikkinchi son katta ekan!")
    




# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# xato 



# mahsulotlar = ["olma", "gosht", "qatiq", "sut", "banan", "sir", 'shokalat', "shirinlik", 'uzuk', 'telefon']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} - mahsulot nomini kiriting:"))
 
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
 
#       print(f"Tanlagan {mahsulot} mahsulotingiz do'konimizda bor!")
#     else:
#         print(f"Tanlagan {mahsulot} mahsulotingiz do'konimizda yo'q")




# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")





# mahsulotlar = ["olma", "gosht", "qatiq", "sut", "banan", "sir", 'shokalat', "shirinlik", 'uzuk', 'telefon']
# savat = []
# for n in range(5):
#  savat.append(input(f"{n+1} - Mahsulot nomini kiriting:"))
# bor_mahsulot = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#       bor_mahsulot.append(mahsulot)
   
#     else:
#        mavjud_emas.append(mahsulot)
       
       
       
# if mavjud_emas:
#    print("Do'konimizda quyidagi mahsulotlar yo'q:") 
# for mahsulot in mavjud_emas:
#  print(mahsulot)     
# else:
#    print("Siz so'ragan mahsulotlarni barchasi bor!")






# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.


# foydalanuvchilar = ["admin", "zarif", "sariqdev", "python", "pamidor"]
# logen = input("Yangi login tanlang:")
# if logen.lower() in foydalanuvchilar:
#         print(f"Ro'yxatda {logen.title()} logini bor! Boshqa login tanlang")
# else:
#         print(f"Xush kelibsiz: {logen}" )



# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

# son = int(input("Butun sonni kiriting:"))

# for n in range(2,11):
#  if not (son%n):
#     print(f" Kiritgan {son} soningiz {n} ga qoldiqsiz bo'linadi!")




# JAVOBLAR
# son = float(input("Juft son kiriting: "))
# if son%2:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")
# Juft son kiriting: 4
# Rahmat!

# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0;
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")
# Yoshingiz nechida?15
# Chipta 10000 so'm
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")
# Birinchi sonni kiriting: 12
# Ikkinchi sonni kiriting: 23
# 12.0<23.0



# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")
# Savatga 1-mahsulotni qo'shing: olma
# Savatga 2-mahsulotni qo'shing: anor
# Savatga 3-mahsulotni qo'shing: un
# Savatga 4-mahsulotni qo'shing: uzum
# Savatga 5-mahsulotni qo'shing: qovun
# Do'konimizda olma bor
# Do'konimizda anor yo'q
# Do'konimizda un bor
# Do'konimizda uzum bor
# Do'konimizda qovun bor
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
# Savatga 1-mahsulotni qo'shing: olma
# Savatga 2-mahsulotni qo'shing: anjir
# Savatga 3-mahsulotni qo'shing: uzum
# Savatga 4-mahsulotni qo'shing: qovun
# Savatga 5-mahsulotni qo'shing: un
# Do'konimizda quyidagi mahsulotlar yo'q:
# anjir





# users = ['alisher','aziza','yasina','umar']

# login = input("Yangi login tanlang: ")

# if login.lower() in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")
# Yangi login tanlang: anvar
# Xush kelibsiz, Anvar!



# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
# Istalgan butun son kiriting: 45
# 45 soni 3 ga qoldiqsiz bo'linadi
# 45 soni 5 ga qoldiqsiz bo'linadi
# 45 soni 9 ga qoldiqsiz bo'linadi