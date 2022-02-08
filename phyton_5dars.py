# # 5 - dars STRING (MATN)
# # sana 25.10.21
# #muallif Zarif ustoz Anvar Narzullayev
# #unicode
# tel = ("🤳")
# print("Men yangi", tel, "oldim")


# # STRING USTIDA AMALLAR STR

# ism = 'Ahmad'
# print("Mening ismim " + ism)

# ism = "Ahad"
# fam = "Qayum"
# print(ism + fam)
# print(ism + ' ' + fam)

# ism = "Ahad"
# fam = "Qayum"
# ism_fam = f"{ism} {fam}"
# print(ism_fam)

# ism = "James"
# familiya = "Bond"
# print(f"salom mening ismim {ism}. {ism} {familiya}")

# #         MAXSUS BELGILAR

# print("Hello World!")
# print("Hello \tWorld!")   # Uzun bo'sh joy tashlaydi
# print("Hello \nWorld!")   # ikki qatorga bo'lib yozadi

#   # String Metodlari.
 
# ism = "james"
# familiya = "bond"
# ism_fam = f"{ism} {familiya}"
# print(ism_fam)
# print(ism_fam.upper()) # Upper harflarni katta harf qilib yozadi.
# print(ism_fam.lower()) # Lower bu harflarni barchasini kichik qilib yozadi
# print(ism_fam.title()) #Title bu har bir so'zni faqat 1- harfini bosh harf  bilan yozadi
# print(ism_fam.capitalize()) # bu capitalize matndagi so'zlarni birinchi so'zni bosh harf bilan boshlaydi.
# meva = "       olma    "
# print(meva)
# print("Men " + meva.lstrip() + "yaxshi ko'raman") #lstrip chap tamondagi bo'shliqni olib tashlaydi
# print("Men " + meva.rstrip()+ " yaxshi ko'raman") #o'ng tamondagi bo'shliqni olib tashlaydi
# print("Men "+ meva.strip() + " yaxshi ko'raman") # Ikki tamonidagi bo'shliqni olib tashlaydi
# print("Men" + meva + "yaxshi ko'raman")



# # INPUT FOYDALANUVCHINING NOMI

# ism = input("Ismingiz nima?")
# # print("Asalomu alaykum" + ism)
# print("Assalomu alaykum, " + ism.title())
# ism = input("Ismingiz nima? \n>>>")
# print("Assalomu alaykum, " + ism.title())

#       VAZIFA
1.

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# #2
# print(kocha, "ko'chasi,")
# print(mahalla, "mahallasi,")
# print(tuman, "tumani,")
# print(viloyat, "viloyati")

#3
# print("Quyidagilarni to'ldiring:")
# kocha = input("ko'changiz:")
# mahalla = input("mahallangiz:")
# tuman = input("tumaningiz:")
# viloyat = input("viloyatingiz:")
# print(kocha + " ko'changiz,", mahalla + " mahallangiz,", tuman + " tumaningiz,", viloyat + " viloyatingiz,")

#4
# print("Quyidagilarni to'ldiring:")
# kocha = input("Ko'changizni nomini kiriting:")
# mahalla = input("Mahallangizni nomini kiriting:")
# tuman = input("Tumaningiz nomini kiriting:")
# shahar = input("Shaharingizni nomini kiriting:")
# print(kocha + " ko'changiz\n" + mahalla +  " mahallangiz \n" + tuman +  " tumaningiz\n" + shahar +  " shaharingiz")
#Upper() barcha harflar katta bilan
# print((kocha + " ko'changiz\n" + mahalla +  " mahallangiz \n" + tuman +  " tumaningiz\n" + shahar +  " shaharingiz").upper())
#5
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
# yangi_manzil = (f"{kocha} ko'changiz, {mahalla} mahallangiz, {tuman} tumaningiz, {viloyat} viloyatingiz.").lower()
yangi_manzil = (f"{kocha} ko'changiz, {mahalla} mahallangiz, {tuman} tumaningiz, {viloyat} viloyatingiz.").title()
# yangi_manzil = (f"{kocha} ko'changiz, {mahalla} mahallangiz, {tuman} tumaningiz, {viloyat} viloyatingiz.").upper()
# yangi_manzil = (f"{kocha} ko'changiz, {mahalla} mahallangiz, {tuman} tumaningiz, {viloyat} viloyatingiz.").capitalize()
print(yangi_manzil)
