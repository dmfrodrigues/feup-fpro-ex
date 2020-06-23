#
# DESCRIPTION of exercise 6: 
#
#    Write a function get_positions that receives two arguments: word_list (a list of strings) and sentence (a string). 
#    The second argument contains 2 words that appear in 1st argument concatenated with a single space in between. 
#    The function returns a string with the position in the list of the first word and the position of the second word 
#     in the list, separated by a single space. Positions start counting at zero.
#
#    For example: get_positions(["hello", "world", "lousy"], "lousy world") returns the string "2 1" 
#
# Do NOT alter the function prototype given
#
# PASTE your code inside the function block below, paying atention to the right indentation
#
# Don't forget that your program should use the return keyword in the last instruction 
# to return the appropriate value
#

def get_positions(word_list, sentence):
    """
    build the highest possible number out of the combination of 3 digits
    """
    #### MY CODE STARTS HERE ######################################
    vtr = sentence.split()
    s1 = -1
    s2 = -1
    for i in range(len(word_list)):
        if word_list[i] == vtr[0] and s1 == -1:
            s1 = i
        if word_list[i] == vtr[1] and s2 == -1:
            s2 = i
    return "%d %d"%(s1, s2)
    
    #### MY CODE ENDS HERE ########################################
    
print(get_positions(["hello", "world", "lousy"], "lousy world"))