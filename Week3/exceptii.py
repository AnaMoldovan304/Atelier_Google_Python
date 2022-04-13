variabila = input("Introdu un numar: ")
#este_intreg = int(variabila)
my_int = None
try:
    este_intreg = int(variabila)
    if my_int is None:
        raise ValueError
except ValueError as e:
    print("Eroare de valoare", e)
except Exception as e:
    #print(e.__doc__) #iti da tipul de eroare
    print('a aparut o eroare', e)
else:
    print("nu exista exceptii intalnite")
finally:
    print('Se ruleaza oricum')