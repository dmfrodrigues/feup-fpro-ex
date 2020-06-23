import math as mt
def tfidf(documents):
    N = len(documents)
    dct = {}
    for str in documents:
        for w in str.lower().split(' '):
            if w not in dct:
                dct[w] = [0]*len(documents)
    
    for i in range(N):
        d = documents[i]
        for w in d.lower().split(' '):
            dct[w][i] += 1
    
    for w in dct:
        n = sum(1 for x in dct[w] if x != 0)
        idf = mt.log(N/n)
        dct[w] = [round(x*idf,3) for x in dct[w]]

    return dct

in_ = ["To be or not to be", "Impossible is a word to be found only in the dictionary of fools", "There is nothing impossible to him who will try"]
out = tfidf(in_)
print(out)
expected = {'to': [0.0, 0.0, 0.0], 'be': [0.811, 0.405, 0.0], 'or': [1.099, 0.0, 0.0], 'not': [1.099, 0.0, 0.0],\
            'impossible': [0.0, 0.405, 0.405], 'is': [0.0, 0.405, 0.405], 'a': [0.0, 1.099, 0.0], 'word': [0.0, 1.099, 0.0],\
            'found': [0.0, 1.099, 0.0], 'only': [0.0, 1.099, 0.0], 'in': [0.0, 1.099, 0.0], 'the': [0.0, 1.099, 0.0],\
            'dictionary': [0.0, 1.099, 0.0], 'of': [0.0, 1.099, 0.0], 'fools': [0.0, 1.099, 0.0], 'there': [0.0, 0.0, 1.099],\
            'nothing': [0.0, 0.0, 1.099], 'him': [0.0, 0.0, 1.099], 'who': [0.0, 0.0, 1.099], 'will': [0.0, 0.0, 1.099], 'try': [0.0, 0.0, 1.099]}
print(out == expected)