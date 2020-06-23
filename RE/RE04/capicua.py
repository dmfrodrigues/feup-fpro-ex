#
# DESCRIPTION of exercise 6: 
#
#   Write a program that given an integer in the variable num, provided by the user,
#   computes its reverse (the number with the digits by the reverse order).
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def capicua():
    result = "Not yet implemented"

#### MY CODE STARTS HERE ######################################
# 
    inp = int(input("Num to reverse:"))
    num = inp
    pal = 0
    while num != 0:
        pal *= 10
        
        digit = num % 10
        pal += digit
        num //= 10
        
    if pal == inp:
        result = "%d is a palindrome."%inp
    else:
        result = "%d is not a palindrome."%inp
# 
#### MY CODE ENDS HERE ########################################
    
    return result



print(capicua())
