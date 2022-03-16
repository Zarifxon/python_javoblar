# AMALIYOT
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur 
# shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi 
# ma'lumotni konsolga chiqaring.

# m_shaxs0 = {
#    'shaxs':'Navoiy',
#    'haq': "1441 -yil tug'ilgan, 1501-til olamdan o'tgan"
#    }

# m_shaxs1 = {
#    'shaxs':'Anvar Narz',
#   'haq' : "1983 yil 23-noyabrda tugilgan"
#    }
# m_shaxs2 = {
#    'shaxs':'Avloniy',
#    'haq': "878-yil tug'ilgan 1934-yil vafot etgan"

#    }
# m_shaxs3 = {
#    'shaxs':"Zarif Mirzo",
#    'haq': "1995 yil 27 -dekabrda tug'ilgan"
#    }
# m_shaxss = [m_shaxs0, m_shaxs1, m_shaxs2, m_shaxs3]
# for m_shaxs in m_shaxss:
#     print(f"{m_shaxs['shaxs']}: "
#           f"{m_shaxs['haq']} haqida ")



# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari
#  ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va
#  uning asarlarini konsolga chiqaring.
# m_shaxs0 = {
#    'shaxs':'Navoiy',
#    'haq': "1441 -yil tug'ilgan, 1501-til olamdan o'tgan",
#    'm_asar': "Hamsa dostoni"
#    }

# m_shaxs1 = {
#    'shaxs':'Anvar Narz',
#   'haq' : "1983 yil 23-noyabrda tugilgan",
#   'm_asar':"Pythonda dasturlash asoslari"
#    }
# m_shaxs2 = {
#    'shaxs':'Avloniy',
#    'haq': "878-yil tug'ilgan 1934-yil vafot etgan",
#    'm_asar':"Toshkent tongi"
#    }
# m_shaxs3 = {
#    'shaxs':"Zarif Mirzo",
#    'haq': "1995 yil 27 -dekabrda tug'ilgan",
#    'm_asar': "Karvon studio"
#    }
# m_shaxss = [m_shaxs0, m_shaxs1, m_shaxs2, m_shaxs3]
# for m_shaxs in m_shaxss:
#     print(f"{m_shaxs['shaxs'].upper()}: "
#           f"{m_shaxs['haq']} haqida "
#           f"{m_shaxs['m_asar'].upper()} asarlari")

# Oila a'zolaringiz (do'stlaringiz) dan
#  3 ta sevimli kino-seriali haqida so'rang.
#  Do'stingiz ismi kalit, uning sevimli kinolarini 
#  esa ro'yxat ko'rinishida lug'artga saqlang.
#  Natijani konsolga chiqaring.
# ism = []
# ism = input("Ismingni kirit:")
# kino = []  
# kino = input("Sevimli kinoni kirit:")
   

# kinolar = {
#         'ali': ["jumong", 'iris', 'hayot'],
#         'vali':['telba', 'taqdir', 'sevgi'],
#         'sali':["ishq", "love", "it"]
#         }
# for kalit, kinolar in kinolar.items():
#     print(f"\n {kalit.title()}ning sevimli kinosi:")
#     for kino in kinolar:
#         print(kino.upper())
# Davlatlar degan lug'at yarating, lug'at ichida bir 
# nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
#  Har bir davlat haqida ma'lumotni konsolga chiqaring.
davlats ={
'uzb':{
        'poytaxt': "toshkent",
        'mus':"1991"
        },
'ros':{
    'poytaxt':"maskva",
    'mus':1000 },
'baa':{
        'poytaxti': "dubay",
        'mus': 1500}
    }


for davlat, info in davlats.items():
    if davlat.lower()=='uzb':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {davlats['poytaxt'].title()}",
          f"\nMustaqilligi: {davlats['mus']}")
#         

# for kalit, qiymat in davlats.items():
#     print(f"{ 'kalit'} poytaxti: {'qiymat'} bo'ladi")

    # for dav in davlats:
    #     print(dav.upper())
# Yuqoridagi dasturga o'zgartirish kiriting:
#     konsolga barcha davlatlarni emas, foydalanuvchi 
#     so'ragan davlat haqida ma'lumot bering.
#     Agar davlat sizning lug'atingizda mavjud bo'lmasa,
#     "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.









# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     if davlat.lower()=='aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")

# O'zbekistonning poytaxti Toshkent
# Hududi: 448978 kv.km
# Aholisi: 33000000
# Pul birligi: so'm

# Rossiyaning poytaxti Moskva
# Hududi: 17098246 kv.km
# Aholisi: 144000000
# Pul birligi: rubl

# AQSHning poytaxti Vashington
# Hududi: 9631418 kv.km
# Aholisi: 327000000
# Pul birligi: dollar

# Malayziyaning poytaxti Kuala-Lumpur
# Hududi: 329750 kv.km
# Aholisi: 25000000
# Pul birligi: rinngit
# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")
# Davlat nomini kiriting: malayziya

# Malayziyaning poytaxti Kuala-Lumpur
# Hududi: 329750 kv.km
# Aholisi: 25000000
# Pul birligi: rinngit