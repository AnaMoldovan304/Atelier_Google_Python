def your_function(*var, **pwargs):
    suma = 0
    for item in var:
        if type(item) == int or type(item) == float:
            suma += item
    return suma


#print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
#print(your_function())
#print(your_function(2, 4, 'abc', param_1=2))

def functie_2(n):
    suma = 0
    sum_par = 0
    sum_imp = 0
    for i in range(n + 1):
        suma += i
        if i % 2 == 0:
            sum_par += i
        else:
            sum_imp += i
    return suma, sum_par, sum_imp

#print(functie_2(4))


def functie_3():
    n = input("Scrie o valoare: ")
    try:
        m = int(n)
        return n
    except:
        return 0


print(functie_3())