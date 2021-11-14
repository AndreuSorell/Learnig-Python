def last(s):
    palabras = s.split()
    """ split es para convertir una cadena en una list por palaba y no por character """
    lista1 = []
    for palabra in palabras:
        lista1.append(palabra[-1])
    cadena_ordenada = sorted(lista1)
    
    lista_ordenada = []
    for char in cadena_ordenada:
        i = 0
        for palabra in palabras:
            if char == palabra[-1]:
                lista_ordenada.append(palabra)
                palabras.pop(i)
                break
            i += 1

    return lista_ordenada


print(last("man i need a taxi up to ubud"))
#["a", "need", "ubud", "i", "taxi", "man", "to", "up"]
#last("take bintang and a dance please")
#["a", "and", "take", "dance", "please", "bintang"]