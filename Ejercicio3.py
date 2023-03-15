def ejercicio3(string):
    l = string.split(' ')
    s = set(l)
    d = dict()
    for palabra in s:
        cant = 0
        for i in l:
            if i == palabra:
                cant += 1
        d[palabra]= cant
    return d
