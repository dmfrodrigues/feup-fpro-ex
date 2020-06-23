def add(f, n, s, b, c):
    if c: return ""
    elif b: return "%s\n"%f
    else: return "%s:%d:%s\n"%(f, n, s)

def grep(pattern, files_list, flags=''):
    flags = flags.split()
    if '-i' in flags: pattern = pattern.lower()
    ret = ""
    for f in files_list:
        with open(f) as strm:
            cont = strm.readlines()
            counter = 0
            for i in range(len(cont)):
                curr = cont[i].strip()
                if '-i' in flags: curr = curr.lower()
                if '-x' not in flags:
                    if (pattern in curr) != ('-v' in flags):
                        ret += add(f, i+1, cont[i].strip(), '-l' in flags, '-c' in flags)
                        counter += 1
                        if '-l' in flags: break
                else:
                    if (pattern == curr) != ('-v' in flags):
                        ret += add(f, i+1, cont[i].strip(), '-l' in flags, '-c' in flags)
                        counter += 1
                        if '-l' in flags: break
            if '-c' in flags and counter != 0:
                ret += "%s:%d\n"%(f,counter)
    return ret[:-1]

#print(grep('Hello', ['file1g.txt', 'file2g.txt'], ''))
print(grep('Hello', ['file1g.txt', 'file2g.txt'], '') == \
    'file1g.txt:1:"Hello, World!" program is as simple as writing print("Hello, World!").\n'+\
    'file2g.txt:2:Hello world!\n'+\
    'file2g.txt:3:Hello')
print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i') == \
    'file1g.txt:1:"Hello, World!" program is as simple as writing print("Hello, World!").\n'+\
    'file1g.txt:3:Instead of implementing the "hello, world" program ...\n'+\
    'file2g.txt:2:Hello world!\n'+\
    'file2g.txt:3:Hello\n'+\
    'file2g.txt:4:another hello')
print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i -x') == "file2g.txt:3:Hello")
print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i -v') == \
    "file1g.txt:2:So, we are going to write a different program.\n"+\
    "file1g.txt:4:Let's try to implement the grep function :)\n"+\
    "file2g.txt:1:I am file2\n"+\
    "file2g.txt:5:End of file")
#print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i -l'))
print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i -l') == "file1g.txt\nfile2g.txt")
print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i -c') == "file1g.txt:2\nfile2g.txt:3")
print(grep('Hellooo', ['file1g.txt', 'file2g.txt'], '') == '')