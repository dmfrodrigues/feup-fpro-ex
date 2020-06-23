#
# DESCRIPTION of exercise 3: 
#
#   Write a Python program which “plays” the known game FizzBuzz over a sequence of integers 
#   from 0 to an integer n provided by the user. 
#   See Google Docs for implementation details.
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def fizz_buzz():
    result = "Not yet implemented"
    
#### MY CODE STARTS HERE ######################################
# 
# 

    n = int(input("n:"))
    result = "1"
    for i in range(2, n+1):
        if i%(3*5) == 0:
            continue
        elif i%3 == 0:
            result += " Fizz"
        elif i%5 == 0:
            result += " Buzz"
        else:
            result += " %d"%i
        

#
# 
#### MY CODE ENDS HERE ########################################
    
    return result

print(fizz_buzz())