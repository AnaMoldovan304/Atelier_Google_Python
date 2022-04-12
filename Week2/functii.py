# print("Mesaj consola")
# variabila = 1
# print('Mesajul mr {}'.format(variabila))
# raspuns_utilizator = input("Care este numele tau: ")
# print(raspuns_utilizator)
# def functia_mea(param_1):
#     pass

# def suma(a: int, b: int = 1) -> (int, int):
#     """
#     #3 " + enter -  sa ai explicatii mai ample
#     :param a: prim nr
#     :param b: sec nr
#     :return: suma, dif
#     """
#     if type(a) == str:
#         return a, b
#     return a+b, a-b
#
#
# suma_mea, diferenta = suma(3, 4) #ctrl + P - vezi ce tip de date
# print(suma_mea, diferenta)
#
# def my_function(*param_1):
#     print(type(param_1))
#     return param_1
#
# print(my_function("string", 'string1', 'string2'))

# def suma_nr_infinit(param1, param2, *var): # *var este tuplu
#     suma=0
#     for item in var:
#         suma += item
#     return suma
#
#
# print(suma_nr_infinit(1, 2, 3, 4, 5, 6, 7))

# def catalog(param1, *args, **kwargs):
#     print(type(kwargs))
#     return param1, args, kwargs
#
# print(catalog(1,nume="Ion",prenume="Vasile", varsta="12"))

# def suma(a, b):
#     a = diferenta(a, b)
#     return a + b
#
#
# def diferenta(a, b):
#     return a-b
#
#
# print(suma(diferenta(1,2), 2))
# print(suma(1, 2))

a,b = 10, 20
# min = None
# if a<b:
#     min = a
# else:
#     min = b

#min = a if a < b else b
#print(min)
# lista_produse = ['ciocolata', 'suc', 'paine', 'mere', 'apa']
# lista_noua = []
# for x in lista_produse:
#     if "a" in x:
#         lista_noua.append(x)
#lista_noua = [x for x in lista_produse if 'a' in x]
# lista_noua = [x if 'a' in x else 'b' for x in lista_produse]
# print(lista_noua)

min = None
if suma := a + b:
    print(suma)

import datetime
date = '05/05/05'
print(datetime.datetime.strptime(date, '%d/%m/%y'))