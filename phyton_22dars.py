# 22- dars MOSLASHUVCHAN FUNKSIYA *ARGS, **kwargs:
    
# def summa(*sonlar):
#    """Kiritilgan sonlarning yig'indisini qaytaruvchi funksiya"""
#    yigindi = 0
#    for son in sonlar:
#        yigindi += son
#    return yigindi
# print(summa(1,2))
# print(summa(1,2,3))

# def summa(*sonlar):
#     """Kiritilgan sonlarning yig'indisini qaytaruvchi funksiya"""
#     return sum(sonlar)
# print(summa(1,2,3,4,5,6))

# def summa(x,y, *sonlar):
#     """Kiritilgan sonlarning yig'indisini qaytaruvchi funksiya"""
#     return x+y+sum(sonlar)
# print(summa(1,2,3))
# print(summa(9,10,50))


# **KWARGS usuli

def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at kor'inishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar
avto1= avto_info("GM", "malibu", rang="qora", yil=2018)
avto2=avto_info("Kia", "K5", rangi='oq', narxi='1000', yili=2022)
print(avto2)




