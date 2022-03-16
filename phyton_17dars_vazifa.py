# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# print("Kitoblar ro'yxatini tuzuvchi dastur ")
# savol = "Yaxshi ko'rgan kitobizni kiriting:"
# savol += ("Tugatish uchun [stop] ni bosing:  ")
# qiymat = ' '
# while qiymat != 'stop':
#         qiymat = input(savol)  
#         if qiymat != 'stop':
    
#             print(qiymat)





# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 
#     7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
#     18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
#     Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin
#     va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb
#     yozganda dastur to'xtasin (ikkita shartni ham tekshiring).





# print("Muzeyga kirish uchun to'lov")
# savol = "Yoshingizni kiriting:  "
# savol += ("Hisobni yopish uchun [Exit] yoki [Quit] ni kiriting   ")
# qiymat = ' '
# while True:
#     qiymat = (input(savol))
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
       
#     yosh = int(qiymat)
#     if yosh<7:
#         narx = 2000
#     if 7< yosh <18:
#         narx = 3000
#     if 18< yosh<65:
#         narx = 10000
#     if yosh>65:
#         narx = 0
#     print(f"Muzeyga kirish narxi {yosh}-yosh bo'lganlarga {narx} so'm. Haridingiz uchun rahmat")
    

    


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    