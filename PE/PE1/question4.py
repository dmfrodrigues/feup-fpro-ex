LE = int(input("LE="))
RE = int(input("RE="))
PE = int(input("PE="))
TE = int(input("TE="))

if 0 <= LE and LE <= 100 and \
   0 <= RE and RE <= 100 and \
   0 <= PE and PE <= 100 and \
   0 <= TE and TE <= 100:
    if PE < 40 or TE < 40:
        print("RFC")
    else:
        grade = int((LE + RE + 4*PE + 4*TE)/50)
        print(grade)
else:
    print("Input error")
