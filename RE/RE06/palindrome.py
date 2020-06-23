
def is_palindrome(str):
    if(len(str) < 2 or str != str[::-1]):
        return False
    return True

def palindrome(astring):
    N = len(astring)
    counter = 0
    for l in range(0, N+1):
        for r in range(l, N+1):
            if is_palindrome(astring[l:r]):
                counter += 1
    return "For string '%s': %d palindrome substrings"%(astring, counter)

#astring = input("astring:")
#print(palindrome(astring))
