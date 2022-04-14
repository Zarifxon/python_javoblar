# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

# def kopaytma(*sonlar):
#     """Kiritilgan sonlarni ko'paytmasini qaytaruvchi funksiya"""
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
# print(kopaytma(1,3,4))
# # Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
#  Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy 
#  ko'rinishda istalgancha berilishi mumkin bo'lsin.
def talaba_tab(ism, familiya, **malumotlar):
    """Talabalar haqidagi malumotlarni qaytaruvchi funksiya"""
    malumotlar['ism'] =ism
    malumotlar['familiya']=familiya
    return malumotlar
talaba1 = talaba_tab("Oybek", "Suyunov", yoshi =24, bahosi =5)
talaba2= talaba_tab("Fozil", "Maxanov", yoshi =26, bahosi=71)
print(talaba1)