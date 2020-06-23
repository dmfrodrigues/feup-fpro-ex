#
# DESCRIPTION of exercise 4: 
#
#   Write a program that checks if a triangle is equilateral, isosceles or scalene, 
#   with the 3 sides provided by the user, each one in different an input() statement. 
#   See Google Docs for implementation details.
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value

def triangle_form():
    result = "Not yet implemented"
    
#### MY CODE STARTS HERE ######################################
# 

    s1 = int(input("s1:"))
    s2 = int(input("s2:"))
    s3 = int(input("s3:"))
    
    if s1+s2 > s3 or s1+s3 > s2 or s2+s3 > s1:
        result = "Not a triangle"
    elif s1 == s2 and s1 == s3:
        result = "Equilateral"
    elif s1 == s2 or s1 == s3 or s2 == s3:
        result = "Isosceles"
    else:
        result = "Scalene"

# 
#### MY CODE ENDS HERE ########################################
    
    return result

print(triangle_form())