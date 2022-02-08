# # 8-dars Vazifa
# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
dav = ['Samarqand', 'Toshkent',  'Navoiy', 'Jizzax']
# print(dav)
#N: ['Toshkent', 'Samarqand', 'Navoiy', 'Jizzax']

# Ro'yxatning uzunligini konsolga chiqaring
# print("Shaharlar soni:", len(dav))
#N:Shaharlar soni: 4

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(dav))
#N: ['Jizzax', 'Navoiy', 'Samarqand', 'Toshkent']

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

# print(sorted(dav, reverse=True))
# ['Toshkent', 'Samarqand', 'Navoiy', 'Jizzax']
# print(sorted(dav))
#N: ['Jizzax', 'Navoiy', 'Samarqand', 'Toshkent']
# Asl ro'yxatni qaytadan konsolga chiqaring
# print(dav)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# dav.reverse()
# print(dav)
# print(sorted(dav))
#N: ['Jizzax', 'Navoiy', 'Samarqand', 'Toshkent']

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# dav = ['Toshkent', 'Samarqand', 'Navoiy', 'Jizzax']
# dav.sort()
# print("Alfabit bo'yicha:", dav)
#N: Alfabit bo'yicha: ['Jizzax', 'Navoiy', 'Samarqand', 'Toshkent']

# dav.sort(reverse=True)
# print("Alfabitga teskari:",dav)
#N:Alfabitga teskari: ['Toshkent', 'Samarqand', 'Navoiy', 'Jizzax']

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# son = list(range(120,1200,2))
# print(son)
# #N: [120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, .......  .. 1194, 1196, 1198]
# jami = sum(son)

# # Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print(jami)
#N: 355860
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# kichik = min(son)
# print(kichik)
# #N: 120
# katta = max(son)
# print(katta)
#N: 1198
# ayirma = katta - kichik
# print(ayirma)
# #N: 1078
# Ro'yxatdagi elementlar sonini hisoblang
# print("Ro'yxatni uzunligi:", len(son))
#N: Ro'yxatni uzunligi: 540

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# print("Boshidan 20ta:", son[0:20], "O'rtasidan 20 ta :", son[270:290], "Oxiridan 20 ta:", son[520:540])
# N : Boshidan 20ta: [120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158] 
# O'rtasidan 20 ta : [660, 662, 664, 666, 668, 670, 672, 674, 676, 678, 680, 682, 684, 686, 688, 690, 692, 694, 696, 698] 
# Oxiridan 20 ta: [1160, 1162, 1164, 1166, 1168, 1170, 1172, 1174, 1176, 1178, 1180, 1182, 1184, 1186, 1188, 1190, 1192, 1194, 1196, 1198]

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['Osh','Shashlik', 'Barak', 'Somsa', 'Sumalak']
# print(taomlar)
# # N: ['Osh', 'Shashlik', 'Barak', 'Somsa', 'Sumalak']

# # nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta = taomlar[3:5]
# print("Nonushtaga:", nonushta)
# # N : Nonushtaga: ['Somsa', 'Sumalak']

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# del taomlar[2]
nonushta = taomlar
# print(nonushta)
nonushta.append("sho'rvo")
nonushta.append("sir")
# print(nonushta)
#N: ['Osh', 'Shashlik', 'Somsa', 'Sumalak', "sho'rvo", 'sir']
# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(taomlar)
# print(nonushta)
# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta =('Osh', 'Shashlik', 'Somsa', 'Sumalak', "sho'rvo", 'sir')
# print(nonushta)
nonushta[0] = "qaymoq va non"
print(nonushta)
#N: TypeError: 'tuple' object does not support item assignment