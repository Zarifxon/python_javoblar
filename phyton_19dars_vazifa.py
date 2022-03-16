# 1 Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def ism_yosh(ism, yosh):
#     """Ism va yoshni foydalanuvchidan qabul qilib olib tug'ulgann yilini hisoblovchi funksiya"""
#     print(f"Sizning ismingiz {ism.title()}." ,
#           f"Tug'ulgan yilingiz: {2021-yosh}")
   
    
     # Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
    
# def son_daraja(son):
#     """Foydalanuvhcidan qiymatni olib uning kvadratini va kubini chiqaruvchi funksiya"""
#     print(f" Siz kiritgan son : {son}ga teng, {son} ning kvadrati: {(son)**2} ga " ,
#          f"kubi esa {(son)**3} ga teng")




# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def toq_juft(son):
#     """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2==0:
#         print(f"Siz kiritga raqam {son}ga teng. Bu raqam 'JUFT'")
#     else:
#          print(f"Siz kiritga raqam {son} 'TOQ' ")
    
        

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
#  Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.


        
     
        
     
# def daraja(x,n):
#     """darajani hisobla"""
#     print(f"{x**n} ga teng")
        
      
        # Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
        
# def daraja(x,n=2):
#     """darajani hisobla"""
#     print(f"{x**n} ga teng")      
        
# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan
 # sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
 # Natijalarni konsolga chiqaring.

def qol(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son}ni {n}ga qoldiqsiz bo'linadi")
        
    
# 20ni 2ga qoldiqsiz bo'linadi
# 20ni 4ga qoldiqsiz bo'linadi
# 20ni 5ga qoldiqsiz bo'linadi
# 20ni 10ga qoldiqsiz bo'linadi

# qol(100)
# 100ni 2ga qoldiqsiz bo'linadi
# 100ni 4ga qoldiqsiz bo'linadi
# 100ni 5ga qoldiqsiz bo'linadi
# 100ni 10ga qoldiqsiz bo'linadi

# qol(99)
# 99ni 3ga qoldiqsiz bo'linadi
# 99ni 9ga qoldiqsiz bo'linadi