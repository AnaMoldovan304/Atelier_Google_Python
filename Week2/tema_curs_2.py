lista1 = [7,8,9,2,3,1,4,10,5,6]
lista2 = list(lista1) #creare alta lista ca sa nu modificam lista initiala
print(lista2)
lista2.sort()
print(lista2)  # lista ordonata ascendent
lista2.reverse()
print(lista2)        # lista ordonata descendent
print(lista2[0:10:2]) #numere pare
print(lista2[1:10:2]) #numere impare
print(lista2[1:10:3]) #multipli de 3