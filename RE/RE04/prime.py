#
# DESCRIPTION of exercise 2: 
#
#   Write a program that takes a single integer n provided by the user and returns True, 
#   when it is a prime number, and False otherwise.
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def is_prime():
    result = "Not yet implemented"
    
#### MY CODE STARTS HERE ######################################
# 

    n = int(input("is_prime:"))
    
    if n == 0 or n == 1:
        result = False
    else:
        result = True
        for i in range(2, n):
            if n%i == 0:
                result = False
                break

# 
#### MY CODE ENDS HERE ########################################
    
    return result


while True:
    print(is_prime())
