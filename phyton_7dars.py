# # 7- dars
# # List - ro'yxat
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] #mevalar ro'yxati matn
# narxlar = [12000, 18000, 10900, 22000] #narxlar ro'yxati son
# sonlar = ['bir', 'ikki', 3, 4, 5, 6] #sonlar va matnlar ro'yxati
# ismlar = [] # bo'sh ro'yxat

# APPEND() METODI BU RO'YXATNI OXIRIGA ELEMENT QO'SHADI
# mevalar.append('uzum')
# print(mevalar)

# INSERT() METODI LISTNING ISTALGAN QISMIGA ELEMENT QO'SHADI
# mevalar.insert(2, 'xurmo')
# print(mevalar)

#DEL OPERATORI LISTDAGI ELEMENTNI O'CHIRISH  (Indeks) bo'yicha
# cars = ('tiko', "matiz", 'nexia', 'lasetti',)
# print(cars)



# REMOVE OPERATORI LESTDAGI ELEMENTLARNI NOMI BO'YICHA O'CHIRADI
# hayvonlar = ['it', 'mushuk', "qo'y", 'sigir']
# print(hayvonlar)
# ['it', 'mushuk', "qo'y", 'sigir', 'mushuk']
# hayvonlar.remove('mushuk')
# print(hayvonlar)
# ['it', "qo'y", 'sigir', 'mushuk']

# LISTDAGI ELEMENTLARNI SUG'URIB OLISH
#POP ELELEMTI
bozorlik = ['in', 'kartoshka', 'olma', 'piyoz', 'banan']
mahsulot = bozorlik.pop(1)
print(bozorlik)
print(mahsulot)