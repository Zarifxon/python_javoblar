# 18-dars FUNKSIYA
# FUNKSIYA YARATAMIZ
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")


#qiymat qabul qiluvchi funksiya yatatamiz.
# def salom_ber(ism):
#     """Foydalanuvchiga salom beruvchi dastur""" #DOCSTRING
#     print(f'Assalomu alaykum! Hurmatli {ism.title()}')
    
    # DOCSTRING
    # def salom_ber(ism):
    #     """Foydalanuvchidan ismini qabul qilib,
    #     salom beruchi funksiya"""
    #     print(f"Assalomu alaykum, hurmatli {ism.title()}")
        
        #ARGUMENT VA PARAMETR
# def toliq_ism(ism, familiya):
#     """ism va familiyani jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchining ismi: {ism.title()} \n"
#           f"Foydalanuvchining familiyasi: {familiya.title()}")
    
# def yosh_hisobla(ism, t_yil):
#     """Foydalanuvchidan ism va tug'ulgan yilini qabul qilib olib,
#     yoshini hisoblab chiqaruvchi dastur"""
#     print(f"{ism.title()}ning yoshi {2021-t_yil} - yoshda!")



#PARAMETR NOMI BILAN UZATISH
# def yosh_hisobla(ism='Olim',t_yil = 1995):
#      """Foydalanuvchidan ism va tug'ulgan yilini qabul qilib olib,
#      yoshini hisoblab chiqaruvchi dastur"""
#      print(f"{ism.title()}ning yoshi {2021-t_yil} - yoshda!")
     
     
     #STANDART QIYMAT
# def yosh_hisobla(t_yil, joriy_yil=2021):
#   print(f"Siz {joriy_yil-t_yil} yoshdasiz")
         

# FUNKSIYAGA MUROJAT ETISHDA XATOLLIKLAR
# 1-misol xatolikni topish

# def yosh_hisobla(t_yil, joriy_yil=2021):
#     """Tug'ulgan yildan yoshini hisoblaymiz"""
#     print(f"Siz {joriy_yil-t_yil} yoshdasiz")
# t_yil=input("Tug'ulgan yilingizni kiriting:  ")
# yosh_hisobla(t_yil)
      #bundagi hatolik t_yil=int(input("Tug'ulgan yilingizni kiriting:  "))

# 2-misol Xatolikni topish1

# def yosh_hisobla(t_yil, joriy_yil=2021):
#     print(f"Siz {joriy_yil-t_yil} yohsdasiz")
#     # yosh_hisobla(1993)
         
#          #  yosh_hisobla(t_yil, joriy_yil=2021) #joriy      yil kiritilmagan edi.
# # 3-misol
# def salom_ber(ism):
#     """Salom beruvchi funksiya"""
#     print(f"Assalomu alaykum! {ism.title()} ")
    
# salom_ber('hasan')
         
         # hato  salom_ber(): argument kiritilmagan va printda f string ishlatilmagan
         
         
         
         
         # 4-misol
# def toliq_ism(ism,familiya):
#     print(f"Foydalanuvchi ismi: {ism.title()} \n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
    # toliq_ism('olim hakimov')
         
         # hato argumentga buyruq berishda xatolik bor toliq_ism('olim', 'hakimov')
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         