import urllib.request
import re
def longest_word(url):
    with open("words", 'r') as d:
        c = d.readlines()
        c = [s.strip() for s in c]
        dct = set(c)
        r = urllib.request.urlopen(url)
        info = r.read().decode()
        lst = info.split()
        ret = ""
        for w in lst:
            if w in dct and (len(w)>len(ret) or (len(w)==len(ret) and w<ret)):
                ret = w
        return ret

def main():
    print(longest_word("https://en.wikipedia.org/wiki/Monty_Python"))
    print(longest_word("https://web.fe.up.pt/~jlopes/doku.php/teach/fpro/sheet"))

if __name__ == "__main__":
    main()

