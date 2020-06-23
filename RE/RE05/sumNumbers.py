#
# DESCRIPTION of exercise 2: 
#
#   Write a Python function sum_numbers(n) that returns the sum of all positive
#   integers up to and including n. 
# 
#   For example: sum_numbers(10) returns the value 55 (1+2+3+. . . +10)
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value
#

def sum_numbers(n):
    """
    returns the sum of all positive integers up to and including n
    """
    #### MY CODE STARTS HERE ######################################
    ret = 0
    for i in range(1, n+1):
        ret += i
    return ret
    #### MY CODE ENDS HERE ########################################

print(sum_numbers(10))