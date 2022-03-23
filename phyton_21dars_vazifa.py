# Matnlardan iborat ro'yxat qabul qilib, 
# ro'yxatdagi har bir matnning birinchi harfini
#  katta harfga o'zgatiruvchi funksiya yozing.


# def matnlar(matn):
#   for i in range(len(matn)):
#      matn[i] = matn[i].capitalize()
     
# matn1 =["salom yoshlar",'siz', "sizlarni yaxshi ko'raman"]
                  
# matnlar(matn1)
# print(matn1)



#Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan
#  va yangi ro'yxat qaytaradigan qilib o'zgartiring

# def matnlar(matn):
#     matn = matn[:]
#     for i in range(len(matn)):
#       matn[i] = matn[i].capitalize()
#     return matn
# matn1 =["salom yoshlar",'siz', "sizlarni yaxshi ko'raman"]
# yangi_matn1= matnlar(matn1)  
# matnlar(matn1)
# print(matn1)
# print(yangi_matn1)

 # Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan
 # va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=int(baho)
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar =bahola(talabalar)
print(baholar)
print(talabalar)


 
 
 
 