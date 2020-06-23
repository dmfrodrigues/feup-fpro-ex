roman = {'0':0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
def roman_to_integer(astring):
    astring += "0"
    sum = 0
    for i in range(len(astring)-1):
        if roman[astring[i]] >= roman[astring[i+1]]:
            sum += roman[astring[i]]
        else:
            sum -= roman[astring[i]]
    return sum

print(roman_to_integer('LXXXIV'))
print(roman_to_integer('XLIII'))
print(roman_to_integer('MMMCMXCIX'))
