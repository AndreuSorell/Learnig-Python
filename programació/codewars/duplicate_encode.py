def duplicate_encode(word):
    lower_word = word.lower()
    d = {}
    for char in lower_word:
        if not char in d:
            d[char] = '('
        elif char in d:
            d[char] = ')'
    lista = list(lower_word)
    resultado = ''
    for c in lista:
        resultado += d[c]
    return resultado


    


#duplicate_encode("din")
#"((("
duplicate_encode("recede")
#"()()()"
#test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
#test.assert_equals(duplicate_encode("(( @"),"))((")