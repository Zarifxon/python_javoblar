#15 dars LUG'AT ELEMENTLARI BILAN ISHLASH
# .ITEMS() METODI
# talaba = { 
#     'ism':'shamshiyev',
#     'yosh' : 22,
#     'fakultet': 'matematika',
#     'kurs': 4
#     }
# for kalit, qiymat in talaba.items():
#     print(f"kalit {kalit}")
#     print(f"Qiymat : {qiymat}")
# # print(talaba.items())


# telefonlar = {
#     'ali': 'iphoni x',
#     'vali': 'galaxy S9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310'
#     }
# for k , q in telefonlar.items():
#     print(F"{k.title()}ning telefoni {q}")

# .KEYS() METODI
mahsulotlar = {#Do'kondagi mahsulotlar
              'olma': 10000,
              'anor': 20000,
              'uzum': 40000,
              'anjir': 25000,
              'shaftoli': 30000
              }
# for mahsulot in mahsulotlar:
#     print(mahsulotlar.title())


#RO'YXAT VA LUG'AT
# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for m in mahsulotlar:
#     if m in bozorlik:
#         print(f"{m.title()} {mahsulotlar[m]} so'm")



# for buyum in bozorlik:
#     if buyum not in  mahsulotlar:
#         print(f"Kechirasiz, bizda {buyum} yo'q")
        
        
        
        # LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
    
    
    # .VALUES() METODI
   
# telefonlar = {
#     'ali': 'iphoni x',
#     'vali': 'galaxy S9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310'  
#     }
# print(telefonlar.values())


# print('Foydalanuvchilarnining telefonlari:')
# for tel in telefonlar.values():
#     print(tel)
    
# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy S9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310',
#     'hali': 'iphone x',
#     'botir': 'galaxy S9'
#     }
    
# print("Foydalanuvchilarning telefonlari:")
# for tel in telefonlar.values():
#     print(tel)
    
# print("Foydalanuvchining telefonlari:")  
# for tel in set(telefonlar.values()):
#     print(tel)
    
    
    
    
    
    
    
    