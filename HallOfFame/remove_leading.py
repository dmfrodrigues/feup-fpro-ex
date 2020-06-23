def remove_leading(ip):
    ip = "0" + ip
    ip = ip.split(".")
    ret = str(int(ip[0]))
    for i in range(1, len(ip)):
        if ip[i] == "":
            ip[i] = "0"
        ret += "." + str(int(ip[i]))
    return ret

print(remove_leading("255.024.01.01"))
print(remove_leading("192.168.0.24"))
print(remove_leading("...."))