# 20*-dars QIYMAT QAYTARUVCHI FUNKSIYA 

# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# talaba1 = toliq_ism_yasa('Olim', 'Hakimov')
# talaba2 = toliq_ism_yasa('Hakim','Olimov')
# print(f"Darga kelmagan talabalar: {talaba1} va {talaba2}")





# Ixtiyoriy argumentlar

# def toliq_ism_yasa(ism, familiya,otasining_ismi = ''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#         return toliq_ism.title()
# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'olimov')
# print(f"Darga kelmagan talabalar: {talaba1} va {talaba2}")


#Funksuyadan lug'at qaytarish

# def avto_info(make, model, rangi, korobka, yili, narxi=None):
#     avto = {'kompaniya' : make,
#             'model': model,
#             'rang': rangi,
#             'korobka': korobka,
#             'yil': yili,
#             'narx': narxi          
#             }
#     return avto
# avto1 = avto_info('GM', 'Malibu','Qora', 'Avtomat', 2018)
# avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud mashinalar:')
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narxi: {narx}")


# FUNKSIYADAN RO'YXAT QAYTARAMIZ
# def oraliq(min, max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(0,10))
# print(oraliq(10,21))



# def oraliq(min, max, uch):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 2
#     return sonlar
# # print(oraliq(0,10))
# # print(oraliq(10,21))
# print(oraliq(0,21,2))


# FUNKSIYALARNI SIKLDA ISHLATISH
def avto_info(make, model, rangi, korobka, yili, narxi=None):
    avto = {'kompaniya' : make,
            'model': model,
            'rang': rangi,
            'korobka': korobka,
            'yil': yili,
            'narx': narxi          
            }
    return avto
    print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = []
while True:
    print("\n Quyidagi ma'lumotlarni kiriting", end =' ')
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narxi = input("Narxi: ")
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi,))
    javob  = input("Yana avto qo'shasizmi? (yes\no): ")
    if javob == 'no':
        break
        print(avtolar)
    
 
