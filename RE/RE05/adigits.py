#
# DESCRIPTION of exercise 4: 
#
#    Write a Python function adigits that receives 3 strings, each one with a 
#    single character, representing a decimal digit.
#    The function should return the highest integer number that you can assemble 
#    with the 3 digits given as parameters.
#
#    For example: adigits("4", "2", "5") returns the integer 542
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value
#

def adigits(n1, n2, n3):
    """
    build the highest possible number out of the combination of 3 digits
    """
    #### MY CODE STARTS HERE ######################################
    if(n3 > n2):
        tmp = n3
        n3 = n2
        n2 = tmp
    if(n2 > n1):
        tmp = n2
        n2 = n1
        n1 = tmp
    if(n3 > n2):
        tmp = n3
        n3 = n2
        n2 = tmp
        
    ret = 0
    ret = 100*n1 + 10*n2 + n3
    return ret
    #### MY CODE ENDS HERE ########################################
    
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print(adigits(a,b,c))
