def is_palindrome(str):
    if(len(str) < 2 or str != str[::-1]):
        return False
    return True

def palindrome_index(s):
    if is_palindrome(s):
        return -1
    for i in range(len(s)):
        if is_palindrome(s[:i]+s[i+1:]):
            return i
    return -1

print(palindrome_index("aaab"))
print(palindrome_index("tattarrattat"))
