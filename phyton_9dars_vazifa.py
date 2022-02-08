# AMALIYOT
# 1-Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi 
# har bir ismga takrorlanuvchi xabar yozing
# ismlar = ('zarif','Ali','vali')
# for ism in ismlar:
#     print(f"Salom,{ism}")
#N: Salom,zarif
# Salom,Ali
# Salom,vali    
    
# 2-Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi"
#  degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
# print("Kod", len(ismlar), "marta takrorlandi!")
#N:Kod 3 marta takrorlandi!
# # 3- 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar 
# bir elementining kubini yangi qatordan konsolga chiqaring.
# sonlar = list(range(11,100,2))
# print(sonlar)
# #N: [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31,... 93, 95, 97, 99]
# for son in sonlar:
#  print(f"{son} sonning kubi: {son**3}  ga teng ")
 #N: 11 sonning kubi: 1331  ga teng 
# 13 sonning kubi: 2197  ga teng 
# 15 sonning kubi: 3375  ga teng 
# 17 sonning kubi: 4913  ga teng 
# .
# .
# .
# 91 sonning kubi: 753571  ga teng 
# 93 sonning kubi: 804357  ga teng 
# 95 sonning kubi: 857375  ga teng 
# 97 sonning kubi: 912673  ga teng 
# 99 sonning kubi: 970299  ga teng 
# # 4- Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
#  va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kino_sev =[]
# print("5 ta sevimli kinoingiz qaysilar?")
# for k in range(5):
#   kino_sev.append(input(f"{k+1}-kino:"))
#   print(kino_sev)
# #N; 5 ta sevimli kinoingiz qaysilar?

# 1-kino:Ipman
# ['Ipman']

# 2-kino:Brusli
# ['Ipman', 'Brusli']

# 3-kino:Jumong
# ['Ipman', 'Brusli', 'Jumong']

# 4-kino:Taqdir 
# ['Ipman', 'Brusli', 'Jumong', 'Taqdir ']

# 5-kino:Ayiq
# ['Ipman', 'Brusli', 'Jumong', 'Taqdir ', 'Ayiq']
# print("Uzunligi:", len(kino_sev))
#N: Uzunligi: 5


# # 5- Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
#  va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. 
soni = (input("Bugun nechta odam bilan ko'rishdiz:"))
# ismlar = []
# for n in range(soni):
    # ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi:"))
korishganlar_soni =(soni(soni-1))/2

print(korishganlar_soni)
# Ro'yxatni konsolga chiqaring.









