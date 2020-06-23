"""
Given a text -- perhaps a poem, a speech, instructions to bake a cake,
some inspirational verses, etc. -- write a function called summary(text) that given a string text,
returns a tuple with the number of total words, and the number of words that contain at least an "e" (upper or lower case).
    summary("A fool thinks himself to be wise, but a wise man knows himself to be a fool.") returns the tuple: (17, 6)
"""

def summary(text):
    text = text.split()
    n = len(text)
    m = 0
    for s in text:
        if ("e" in s) or ("E" in s):
            m += 1
    return (n,m)

print(summary("A fool thinks himself to be wise, but a wise man knows himself to be a fool."))


