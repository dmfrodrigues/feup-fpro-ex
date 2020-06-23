import re

def count(word, phrase):
    word = word.lower()
    phrase = phrase.lower()
    phrase = re.split(r' |\.|\?', phrase)
    counter = 0
    for i in range(len(phrase)):
        if phrase[i] == word:
            counter += 1
    return counter

#word = input("word:")
#phrase = input("phrase:")
#print(count(word, phrase))
