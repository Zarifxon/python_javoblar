# savat =[]
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

# mahsulot = []
# print("Mahsulotlar ro'yxati dasturi!")
# n=1
# while True:
#     savol = f"{n} - mahsulotni kiriting:  "
#     savat = input(savol)
#     mahsulot.append(savat)
#     javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print(f"Ro'yxat tuzildi-{mahsulot}")
    





# # e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
 # Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
 
 
# print("E Bozor! Mahsulot va uning narxi")
# mahsulot = {}
# ishora =True
# while ishora:
#     ism = input("Mahsulot nomini kiriting:  ")
#     narx = input(f"{ism.title()}ning narxini kiriting:")
#     mahsulot[ism]= int(narx)

#     javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q) ")
#     if javob == "ha":
#        continue
#     else:
#        break
# for ism, narx in mahsulot.items():
#     print(f"Mahsulot va narxdan tashkil topgan dasturimiz yakunlandi! Natija: {ism, narx} ")
        
 
 
 
# # # Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi
#  har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
#  (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa
#   mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# # # 


# print("Ebozor ro'yxatda mavjud bo'lgan mahsulotlarni sotib olasiz")
# ebozor = ['olma', 'karam', 'shaftoli', 'qalam', 'non' ]
# mahsulot = {}
# ishora = True
# while ishora:
#     nom = input("Mahsulotning nomini kiriting:  ")
#     if nom == 'olma':
#         narx = 10000
#     if nom == "karam":
#         narx = 4000
#     if nom == "shaftoli":
#         narx = 12000
#     if nom == "qalam":
#         narx = 1000
#     if nom =="non":
#         narx= 3000
      
#     if nom in ebozor:
#         print(f"Tanlagan {nom.title()}ning narxi {narx} so'm")
#     else:
#         print(f"{nom.title()} mahsuloti Ebozorda yo'q! Boshqa mahsulot kiriting")

savat =[]
while True:
    mahsulot = input("Savatga mahsulot qo'shing:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
    if javob != 'ha':
        break
    buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")


