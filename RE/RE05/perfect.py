#
# DESCRIPTION of exercise 3: 
#
#   Write a Python function is_perfect(n) to check whether a number n is perfect or not.
#   In number theory, a perfect number is a positive integer that is equal to the sum of its proper
#   positive divisors, that is, the sum of its positive divisors excluding the number itself. 
#
#   For example: for n=6 the function returns True, for n=12 returns False, and for n=28 returns True. 
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value
#

def is_perfect(n):
    """
    check whether a number n is perfect 
    """
    #### MY CODE STARTS HERE ######################################
    val = 0
    for i in range(1, n):
        if n%i == 0:
            val += i
    return (val == n)
    #### MY CODE ENDS HERE ########################################
    
while True:
    i = int(input("i:"))
    print(is_perfect(i))