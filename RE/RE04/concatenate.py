#
# DESCRIPTION of exercise 5: 
#
#   Write a program that, given two numbers n1 and n2 provided by the user 
#   (each one in a different input() statement) produces a new number result 
#   from the concatenation of both of them, in the order they are given. 
#   See Google Docs for implementation details.
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def concatenate():
    result = "Not yet implemented"
    
#### MY CODE STARTS HERE ######################################
# 
# 

    n1 = int(input("n1:"))
    n2 = int(input("n2:"))
    
    no_digits = 0
    tmp = n2
    while(tmp != 0):
        no_digits += 1
        tmp //=10
        
    result = n1*(10**no_digits) + n2

#
# 
#### MY CODE ENDS HERE ########################################

    return result

print(concatenate())
