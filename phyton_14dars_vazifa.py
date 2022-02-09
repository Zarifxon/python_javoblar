# AMALIYOT
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan


# oila = {'otam':'Mirzo', 'onam':'Hafiza', 'ayolim':'Marjona'}
# oila['otam'] = 1956, '2-yanvar', 'erkak'
# oila['onam'] = 1961, '12-sentyabr', 'ayol'
# oila['ayolim'] = 2003, '19-fevral', 'ayol'
# # print(oila['otam'])
# # print(oila['onam'])
# # print(oila['ayolim'])
# print(f"Otam {oila['otam']} yilda tug'ulgan,\
#       onam {oila['onam']} yilda tug'ulgan,\
#     ayolim {oila['ayolim']} yilda tug'ilgan")



# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# oila = {'dadm':'Shashlik', 'oyim': 'sutlik osh', 'akam': 'olma','opam':'kalbasa', 'men': 'barak'}
# print(f"Dadamni sevimli taomi {oila['dadm']}ni yaxshi ko'radi!,\
#       Onamni sevimli taomi {oila['oyim']}ni yaxshi ko'radi!,\
#           Akamni sevimli taomi {oila['akam']}")



# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
py = {"if":'Agar', "elif":'aks holda', "lower":"har bir harfni kichik harfga o'tkazadi",\
      "title" : "Har bir so'zning birinchi harfini bosh harf bilan chiqaradi", \
'or': "yoki degani", 'and':"va degani",\
"integer" : "matn ko'rinishidagi ifodani son qiymatiqilib javob qayataradi",\
    "else":' Agar', \
        'append': "Royxatga element qo'shadi", "print":"Yozilgan dasturni ishga tushiradi"}
print(f" So'zlar tarjimasi: {py} degan ma'nolarni bildiradi!")



# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
# kirit = input("Kerakli so'zni kiriting:").lower()
#     print((py.get(kirit)), "so'zning tarjimasi")
# 

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli\
    # ko'rinishda chiqaring.
    
kirit = input("Kerakli so'zni kiriting:").lower()
if kirit in py:
    print((py.get(kirit)), "so'zning tarjimasi")
else:
    print("Bunday so'z yo'q")  
    
    
    
    
    
    
    
    
    
    
    
    