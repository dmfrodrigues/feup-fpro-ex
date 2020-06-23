def translate(astring, table):
    for obj in table:
        astring = astring.replace(str(obj[0]), str(obj[1]))
    return astring

#print(translate("Hello world!", (('a', 1), ('e', 2), ('i', 3),('o', 4), ('u', 5), ('!', ' :)'))))
#print(translate("Testing this string...", ((' ', '--'), ('.','!'), ('i', 'o'), ('t', 'tt'))))
