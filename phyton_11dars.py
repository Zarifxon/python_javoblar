# elif - else - if
# son = int(input("Sonni kiriting:"))
# if son>0: #agar son 0 dan katta bo'lsa,
#   print('Son musbat!')
# elif son<0: # son o dan kichik bo'lsa manfiy son,
#     print('Son manfiy!')
# else:
#     print('Son 0 ga teng!')
    
# yosh = int(input("Yoshingizni kiriting:"))
# if yosh <7:
#     print('Sizga kirish bepul')
# elif yosh<12:
#     print("Sizga kirish puli -5000 so'm")
# else:
#     print("Sizga kirish puli - 10000 so'm")
    
    
    
    
# yosh = int(input("Yoshingiz nechada ?"))
# if yosh<7:
#  print("Sizga bepul")
# elif yosh <12:
#   print("Sizga kirish puli 5000") 
# else:
#     print("Sizga kirish puli {10000} so'm")


# AND VA OR OPERATORI

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni. Kettik ishga")
#     print(True or False)
#     print(True or True)
#     print(False or False)


# AND OPERATORI
# kun = input("Bugun nima kun?>>>")
# harorat = float(input("Havo harorati qanday? "))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# else:
#     print("Uyda dam olamiz!")

# BIR NECHTA SHARTLARNI KETMA KET YOZ'ISH
# yosh = int(input("Yoshingiz nechada?>>>"))
# kun = input("Bugun qaysi kun?>>>")
# if (yosh<7 or yosh>65) and kun=='chorshanba':
#     print('Bugun siz uchun Muzeyga kirish bepul')
# else:
#     print("Sizga Muzeyga kirish puli 10.000 so'm!")
    


# BOOLEAN MA'LUMOTLAR TURI
# narx = 15000
# choy = True
# salat = False
# if choy and salat:
#      narx = narx + 10000
# elif choy or salat:
#      narx = narx+5000
#      print(f"Jami {narx} so'm!")

# SHARTLARNI KETMA KET TEKSHIRISH

# narx = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti= 0

# if choy:
#     print("Mijoz choy oldi,")
#     narx = narx + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narx = narx + 5000
# if non:
#    print("Mijoz non oldi.")
# narx = narx + 2000
# if kompot:
#     print("Mijoz kompot oldi.")
# narx = narx +5000
# if assorti:
#     print("Mijoz assorti oldi")
#     narx = narx +15000


# print(f"Jami {narx} so'm!")



# RO'YXAT TARKIBINI TEKSHIRISH IN OPERATORI
# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# # 'manti' in menyu
# print("False")
# 'osh' in menyu
# print("True")

# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat yeysiz? >>> ")
# if ovqat.lower() in menyu:
#     print("Buyurtma qabul qilindi! Yana nima ovqat buyurasiz:")
# else:
#     print("Afsuski bunday ovqat menyuda yo'q!")

# NOT IN OPERATORI 

# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# 'osh' not in menyu
# print("False")
# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# 'manti' not in menyu
# print("True")

# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat yeysiz?>>>") 
# if ovqat.lower() not in menyu:
#     print("Afsuski bunday ovqat yo'q")
# else:
#     print("Buyurtma qabul qilindi!")


# IKKI RO'YXATNI SOLISHTIRISH

# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin','somsa']
# buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menyu:
#         print(f"Menyuda {taom} bor")
#     else: 
#         print(f"Kechirasiz, menyuda {taom} yo'q")


#RO'YXAT BO'SH EMASLIGINI TEKSHIRISH
# list1 = [1, 2, 3]
# if list1:
#     print("Ro'yxatda elementlar bor")


menyu = ['osh', 'qozonkabob', 'shashlik', 'norin','somsa']
buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menyu:
            print(f"Menyuda {taom} bor")
            
        else:
            print(f"Kechirasiz, menyuda {taom} yo'q")
    else:
            print("Savatchangiz bo'sh")
