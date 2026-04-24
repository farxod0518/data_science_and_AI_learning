# dostlar = ['sardor', 'elyor', 'islom']
# print('salom'+ dostlar[0]+ '.'+ dostlar[1]+ 'bugun choyxonaga borasanmi?'+ dostlar[2]+ 'soat necha')

# sonlar = [3, 5, 0, -10, 15.8]
# print(sonlar[0]+sonlar[1])
# print(sonlar[3]-10)

# t_shaxslar = ['imom Buuxoriy']
# z_shaxslar = ['Elon musk']
# print('men tarixiy shaxslardan '+ t_shaxslar.pop(0)+ ' bilan, zamonamiz shaxslaridan '+ z_shaxslar.pop(0)+ ' bilan suxbatlashishni hoxlayman')

# friends = []
# friends.append('sardor')
# friends.append('elyor')
# friends.append('islom')
# friends.append('mirkomil')
# friends.append('ilhom')
# print(friends)
# friends.remove('sardor')
# friends.remove('mirkomil')
# print(friends)
# friends.insert(0,'anvar')
# friends.append( 'rustam')
# friends.insert(2, 'yashin')
# print(friends)

# mehmonlar = []
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(3))
# print('mehmonga kelganlar ruyxati: ')
# print(mehmonlar)
# print("mehmonga kelmaganlar ruyxati: ")
# print( friends)

# cars = ['audi', 'bmw', 'volvo', 'chevrolet', 'Toyota']
# moshina = 'nexia salom'
# print(moshina.upper())

countries = ['polsha', 'amerika', 'russia', 'canada', 'ukrain', 'uzbekistan', 'kazakistan']
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

# juft_numbers = list(range(120, 1201,2))
# print(sum(juft_numbers))
# print(max(juft_numbers)-min(juft_numbers))
# print(len(juft_numbers))
# print(juft_numbers[:20])
# print(juft_numbers[len(juft_numbers)//2-10:len(juft_numbers)//2+10])
# print(juft_numbers[-20:])

# taomlar = ['tuxum', 'norin', 'osh', 'beshbarmoq', 'kabob']
# breakfast = taomlar[:]
# del breakfast[3]
# breakfast.remove('osh')
# breakfast.append('kofee')
# breakfast.insert(1,'shurva')
# print(taomlar)
# print(breakfast)
# breakfast = tuple(breakfast)
# print(breakfast)
# breakfast[0] = 'non va saryog'

# ismlar = ['rustam', 'anvar', 'olim', 'akbar', 'ilhom']
# i = 0
# for ism in ismlar:
#     print(f"salom {ism}. axvollaring yaxshimi")
#     i = i+1
# print(f"kod {i} marta takrorlandi")

# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(son**3)

# kinolar = []
# for i in range(5):
#     kinolar.append(input(f"{i+1}-yoqtirgan kinoyingizni nomini kiriting: "))

# print(f"siz yoqritgan kinolar: {kinolar}")

# uchrashuvlar = int(input('bugun necha kishi bilan uchrashdingiz: '))
# insonlar = []
# for i in range(1,uchrashuvlar+1):
#     insonlar.append(input(f"{i}-uchrashgan insoningizning ismi nima: "))
# print(f"bugun siz uchrashgan insonlar {insonlar}")

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# login = input('ismingizni kiriting>>>>')
# if login.lower() == 'admin':
#     print('xush kelibsiz Admin. foydalanuvchilar ruyxatini korasizmi.')
# else:
#     print(f"xush kelibsiz {login.title()}.")


# number_1 = float(input('1-sonni kiriting: '))
# number_2 = float(input('2-sonni kiriting: '))
# if number_1 == number_2:
#     print('sonlar teng.')
# else:
#     print('sonlar teng emas.')

# number = int(input('son kiriting: '))
# if number > 0:
#     print(number**(1/2))
# else:
#     print("musbat son kiriitng.")



# yosh bo'yich kinoga kirishga chipta narxini topish.
# son = int(input("juft son kiriting: ")) # juft son so'raymiz va uning juft yoki unday emasligini aniqlaymiz.
# if son%2 == 0:
#     print('raxmat')
# else:
#     print('iltimos juft son kiriting')

# age = int(input("yoshingizni kiriting: "))
# if age <=4 or age >=60:
#     price = 0
# elif age <=18:
#     price = 5000
# else:
#     price = 10000
# print(f"sizga chipta narxi - {price} s\'m")


# 2 ta son so'rash va ularni solishtirish.
# number_1 = float(input("1-sonni kiriting: "))
# number_2 = float(input("2-sonni kiriting: "))
# if number_1>number_2:
#     print("1-son 2-sondan katta")
# elif number_2>number_1:
#     print("2-son 1-sondan katta")
# else:
#     print("sonlar teng.")


# do'konda izlangan mahsulot bor yoki yo'qligi i aniqlovchi dastur.
# products = ['uzum', 'banan', 'nok', 'non', 'suv', 'tuxum', 'suv', 'pamidor', 'bodiring', 'anor']
# savat = []
# exist_products = []
# unexist_products = []
# mahsulot = input('mahsulotni kiriting: ')
# savat.append(mahsulot)
# mahsulot = input('mahsulotni kiriting: ')
# savat.append(mahsulot)
# mahsulot = input('mahsulotni kiriting: ')
# savat.append(mahsulot)
# mahsulot = input('mahsulotni kiriting: ')
# savat.append(mahsulot)
# mahsulot = input('mahsulotni kiriting: ')
# savat.append(mahsulot)
# for product in savat:
#     if product in products:
#         exist_products.append(product)
#     else:
#         unexist_products.append(product)
# if unexist_products:
#     print("bizda")
#     for i in unexist_products:
#         print(i)
#     print("lar mavjud emas")
# else:
#     print("bizda siz so'ragan barcha mahsulotlar mavjud.")


# users = ['sardor', 'farxod', 'anvar', 'ilhom', 'rustam']
# new_user = input('yangi loginni kiriting: ')
# if new_user.lower() in users:
#     print("bunday user mavjud. boshqa ligin tanlang.")
# else:
#     print(f"xush kelibsiz {new_user}")



# number = int(input("butun son kiriting"))
# for i in range(2,10):
#     if number%i==0:
#         print(f"{number} {i} ga bo'limadi.")



# dictionary
# onam = {
#     'ism':"dilrabo",
#     'yosh':50,
#     'manzili':"chirchiq shahri",
#     'yoqtirgan taom':"norin"
# }

# print(f"onamning ismi {onam['ism'].title()}. yoshi {onam['yosh']}-da va hozirda {onam['manzili']}da istiqomat qilmoqda. yoqtirgan taomi esa {onam['yoqtirgan taom']}.")

# yoqtirgan_taomlar = {
#     'onam':"norin",
#     'akam':"osh",
#     'opam':"chuchvara",
#     'yangam':"beshbarmoq",
#     'men':"pichak"
# }
# print(f"onam {yoqtirgan_taomlar['onam']}ni yoqtiradi.")
# print(f"men {yoqtirgan_taomlar['men']}ni yoqtiraman")

# python_lugat = {
#     'str':"string malumot turi",
#     'if':"agar aperatori",
#     'class':"malumot turlari",
#     'loop':"aylantirish"
# }

# question = input("pythondan biror bir narsa so'rang: ")
# print(python_lugat.get(question,'bunday malumot topilmadi.'))


# python_lugat = {
#     'API':'dasturlashdagi so\'z',
#     'str':"string malumot turi",
#     'if':"agar aperatori",
#     'class':"malumot turlari",
#     'loop':"aylantirish",
#     'set':'malimot turi'
# }
# for key, value in sorted(python_lugat.items()):
#     print(f"{key.title()} - {value.title()}")


# countries = {
#     'uzbekistan':'tashkent',
#     'russia':'moskow',
#     'germany':'berlin',
#     'canada':'attawa',
#     'korea':'seoul'
# }
# for key in sorted(countries.keys()):
#     print(key.title())

# for value in sorted(countries.values()):
#     print(value.title())

# ask = input('istalgan davlatni kirtiing: ')
# if ask.lower() in countries.keys():
#     print(f"{countries[ask.lower()].title()}  {ask.title()} ning poytaxti.")
# else:
#     print("bizda bunday malumot yo'q.")


# taomlar = {
#     'osh':35000,
#     'norin':40000,
#     'xalim':50000,
#     'tort':20000,
#     'chuchvara':25000,
#     'pichak':10000
# }
# talab = []
# for i in range(1,4):
#     talab.append(input(f"{i}-buyurtmani kirting:").lower())

# for taom in talab:
#     if taom in taomlar:
#         print(f"{taom} - {taomlar[taom]} so'm")
#     else:
#         print(f"bizda {taom} yo'q")



# bobur = {
#     'ism':'bobur',
#     't_yil':1571,
#     'millati':'uzbek',
#     'u_yil':1645,
#     'asar':"boburnoma"
# }

# tesla = {
#     'ism':'tesla',
#     't_yil':1937,
#     'millati':'ingliz',
#     'u_yil':1989,
#     "asar":"elektr"
# }

# ulugbek = {
#     'ism':"ulug'bek",
#     't_yil':1545,
#     'millati':'uzbek',
#     "u_yil":1602,
#     'asar':"yulduzlar turkumi"
# }

# yusuf = {
#     'ism':'yusuf',
#     't_yil':1965,
#     'millati':'tojik',
#     'u_yil':2007,
#     'asar':"lola qizg'aldoq"
# }

# mashhurlar = []
# mashhurlar.append(bobur)
# mashhurlar.append(tesla)
# mashhurlar.append(ulugbek)
# mashhurlar.append(yusuf)

# for person in mashhurlar:
#     print(f"{person['ism'].title()} {person['t_yil']}-yilda tavallud topgan \n"
#           f"millati - {person['millati']}. {person['u_yil']}-yilda vafot etgan.\n"
#           f"uning mashxur asari {person['asar']}\n"
#           )


# jami = {}

# for i in range(3):
#     lists = []
#     ism = input('ismni kiriting: ')
#     first_ask = input('1-kinoni kiriting: ')
#     lists.append(first_ask)
#     first_ask = input('2-kinoni kiriting: ')
#     lists.append(first_ask)
#     first_ask = input('3-kinoni kiriting: ')
#     lists.append(first_ask)
#     jami[ism] = lists

# print(jami)

# for key, value in jami.items():
#     print(f"{key.title()}ning yoqtirgan kinolari:")
#     for kino in value:
#         print(f"{kino}. ")
    
            
# countries = {
#     'amerika':{
#         'poytaxti':'washington',
#         'aholisi':330000000,
#         'puli':'dollar'
#     },
#     'uzbekistan':{
#         'poytaxti':'tashkent',
#         'aholisi':38000000,
#         "puli":"so'm"
#     },
#     'russia':{
#         "poytaxti":"moskow",
#         "aholisi":140000000,
#         "puli":"rubl"
#     }
# }


# for keys, values in countries.items():
#     print(f"{keys.title()}ning poytaxti {values["poytaxti"]}.\n"
#           f"aholisi {values["aholisi"]} kishi.\n"
#           f"pul birligi esa {values["puli"]}"
#           )


# ask = input("birorta davlatning nomini kiriting: ")
# if ask not in countries.keys():
#     print("kechirasiz bizda bunday davlat haqida malumot yo'q.")
# else:
#     print(f"{ask.title()}ning poytaxti {countries[ask]["poytaxti"]}.\n"
#             f"aholisi {countries[ask]["aholisi"]} kishi.\n"
#             f"pul birligi esa {countries[ask]["puli"]}"
#           )


# kitoblar = []
# savol = "yaxshi ko'rgan kitobingizni yozing. dasturni to'xtatish uchun stop so'zini yozing: "
# answer = None
# while answer !='stop':
#     answer = input(savol)
#     if answer != 'stop':
#         kitoblar.append(answer)
# print(kitoblar)


# savol = "yoshingizni kiriting dasturdan chiqish uchun stop yoki quit deb kiriting: "
# answer = None
# while answer != 'stop' and answer!= 'quit':
#     answer = input(savol)
#     if answer == 'stop' or answer == 'quit':
#         continue
#     else:
#         if int(answer)<=7:
#             print("sizga chipta narxi 2000 so'm")
#         elif int(answer) < 18:
#             print("sizga chipta narxi 3000 so'm")
#         elif int(answer) <65:
#             print("sizga chipta narxi 10000 so'm")
#         else:
#             print("sizga chipta narxi tekin!")


# mahsulotlar = {}
# while True:
#     savol = input("mahsulot kiritishni hoxlaysizmi: (ha/yo'q)")
#     if savol != 'ha':
#         break
#     answer = input("mahsulot nomini kiriting: ")
#     price = float(input(f"{answer}-ning narxini kiriting: "))
#     mahsulotlar[answer] = price
# print(mahsulotlar)


# def full_info(ism,familiya,yosh,tugulgan_yer = None, telefon_number = None):
#     info = {
#         "ism":ism,
#         "familiya":familiya,
#         "yosh":yosh,
#         "tug'ulgan yer":tugulgan_yer,
#         "telefon raqam":telefon_number
#     }
#     return info

# mijozlar = []
# while True:
#     answer = input("mijoz qo'shishni hoxlaysizmi (yes/no) : ")
#     if answer == "no":
#         break
#     ism = input("ismni kiriting:")
#     familiya = input("familiyani kiriting: ")
#     yosh = input("yoshni kiriting: ")
#     tugulgan_yer = input("tug'ulgan yerni kiriting: ")
#     telefon_number = input("telefon numberni kiriting: ")
#     mijozlar.append(full_info(ism,familiya=familiya, yosh=yosh, tugulgan_yer=tugulgan_yer,telefon_number=telefon_number))

# print('mijozlar haqidagi malumotlar.')
# for mijoz in mijozlar:
#     if mijoz["telefon raqam"]:
#         print(f"{mijoz["ism"]} {mijoz['familiya']} {mijoz['yosh']} yoshda {mijoz["tug'ulgan yer"]}da tug'ilgan telefon raqami - {mijoz["telefon raqam"]}")
#     else:
#         print(f"{mijoz['ism']} {mijoz['familiya']} {mijoz['yosh']} yoshda {mijoz["tug'ulgan yer"]}da tutug'ilgan.")


# def return_number(number1, number2,number3):
#     if number1>number2 and number1>number3:
#         return number1
#     elif number2>number1 and number2>number3:
#         return number2
#     elif number3>number1 and number3>number2:
#         return number3
#     elif number1 ==number2 and number2<number3:
#         return number1 and number2
#     elif number1 ==number3 and number2<number3:
#         return number1 and number3
#     elif number3 ==number2 and number1<number3:
#         return number3 and number2
#     else: return number3

# print(list(return_number(2,4,4)))

# def give_tub(min,max):
#     numbers = []
#     number = int(min)
#     if number%2!=1:
#         num+=1
#     while number<int(max):
#         sanovchi = 0
#         for i in range(2,number//2):
#             if number%i ==0:
#                 sanovchi +=1
#                 break
#         if sanovchi ==0:
#             numbers.append(number)
#         number +=2
#     return numbers


# print(give_tub(3,18))



# def give_fibonachi(parametr):
#     number1 = 0
#     number2 = 1
#     fibbonachi = []
#     number = 1
#     while number < parametr:
#         if number <parametr:
#             fibbonachi.append(number)
#         number = number1+number2
#         number1 = number2
#         number2 = number
#     return fibbonachi

# print(give_fibonachi(100))

# def title_give(lists):
#     addicted = []
#     new = lists[:]
#     for i in lists:
#         addicted.append(i.title())
#     return addicted

# salom = ['qalay','yaxshi']
# print(title_give(salom))
# print(salom)


# def bahola(ismlar):
#     baholar = {}
#     for i in ismlar:
#         baho = input(f"Talaba {i.title()}ning bahosini kiriting: ")
#         baholar[i]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)



# def kopaytma(*sonlar):
#     son  = 1
#     for number in sonlar:
#         son *=number
#     return son

# print(kopaytma(1,3,4))
# print(kopaytma(4,2,5,0))



# def student_info(ism, familiya, **malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familiya'] = familiya
#     return malumotlar

# print(student_info("anvar",'nazlullayev', yosh=23, telefor_number = 932444554))




# datetime modul

import datetime as dt

hozir = dt.date.today()
# ikki_hafta = dt.timedelta(days = 14)
# print(hozir)

# for i in range(1,11):
#     print(hozir+i*ikki_hafta)


# hozir = dt.date.today()
# hayit = dt.date(2026,6,20)
# farq = hayit - hozir
# print(farq)



# def finder(years,month,days):
#     hozir = dt.date.today()
#     t_vaqt = dt.date(year=years,month=month,day=days)
#     masofa = (hozir.year-t_vaqt.year,hozir.month-t_vaqt.month,hozir.day-t_vaqt.day)
#     return masofa

# print(finder(2003,3,4))


# telefon raqamni andoza yordamida tekshirish
# import re

# while True:
#     andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
#     answer = input("telefon raqamingizni kiriting")
#     if re.match(andoza,answer):
#         print("sizning telefon raqamingiz qabul qilindi.")
#         print(answer)
#         break
#     else:
#         print("sizning telefon raqamingizda xatolik bor.")
#         continue


# matndan web sahifani ajratib oluvchi dastur.

# andoza = r'https?://\S+'
# matn = "Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"

# natija = re.findall(andoza, matn)
# if natija:
#     for i in natija:
#         print(i)

# for word in matn.split():
#     if re.match(andoza, word):
#         print(word)


# salom world funksiyasini yarat


# make hello world function
def hello_world():
    return "Hello World"    

print(hello_world())



# make 









































