# 18- dars While Ro'yxatlar va Lug'atlar

# ismlar = []
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 #ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n} - do'stingizni ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha' :
#         n+=1
#         continue
#     else:
#         break
# print("Ro'yxat tuzildi")
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
    
    
    
# print("Dostlaringiz yoshini saqlqaymiz!")
# dostlar = {}
# ishora=True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()} ning yoshini kiriting:  ")
#     dostlar[ism]=int(yosh) #ism kalit yosh qiymat
#     javob = input("yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
    
#     for ism, yosh in dostlar.items():
#         print(f"{ism.title()} {yosh} yoshda")



# cars = ['lasetti', 'nexia', 'toyota', 'nexia', 'malibu','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
#     print(cars)


# "RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH"
talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar={}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()} ning bahosini kiriting:   ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba]=baho
    














