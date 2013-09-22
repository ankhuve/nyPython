def räkna():
    lista = ['hej', 'på', 'dig', 'hej', 'dej']
    lista2 = []
    for i in lista:
        lista[lista.index(i)] = lista[lista.index(i)].upper()
        print(lista)
        if i not in lista2:
            lista2.append(i.upper())
    for i in lista2:
        print("Ordet " + str(i).lower() + " fanns", lista.count(i), "gånger i listan.")
    return lista
