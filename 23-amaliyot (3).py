# -*- coding: utf-8 -*-
"""
Created on Sun May  9 00:17:29 2021

@author: Умида
"""

#1
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
#     avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting",end='')
#         kompaniya=input("Ishlab chiqaruvchi: ")
#         model=input("Modeli: ")
#         rangi=input("Rangi: ")
#         korobka=input("Korobka: ")
#         yili=input("Ishlab chiqarilgan yili: ")
#         narhi=input("Narhi: ")    
#         #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#         #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#         avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))    
#         # Yana avto qo'shish-qo'shmaslikni so'raymiz
#         javob = input("Yana avto qo'shasizmi? (yes/no): ")
#         if javob=='no':
#             break
#     return avtolar

# def info_print(avto_info):
#     """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
#           f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
#           f"{avto_info['yil']}-yil, {avto_info['narh']}$")




# #2
# import avto_info_mod # avto_info_mod faylini (modulini) chaqiramiz

# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)


# #3
# import avto_info_mod as aim # avto_info_mod ni qisqa nom aim bilan chaqiramiz

# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# aim.info_print(avto1)


# #4
# from avto_info_mod import avto_info, info_print

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)


# #5
# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# iprint(avto1)


# #6
# from avto_info_mod import *

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)

# #7
# import math

# x=400
# print(math.sqrt(x))


#8
# print(pow(5,5))

# #9
# from math import pi
# print(pi)

# #10
# print(math.log2(8))
# print(math.log10(100))


# #11
# import random as r # random modulini r deb chaqirayapmiz

# son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
# print(son)


# #12
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# print(ism)
# print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz



# #13
# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))


# #14
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)