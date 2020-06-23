def mycomp(obj):
    s = 0
    for i in obj[2]:
        s += i
    s /= len(obj[2])
    return (-s, obj[0], obj[1])

def sort_grades(records):
    return tuple(sorted(records, key=mycomp))

#print(sort_grades(  (('João', 'up20186042', (90, 87)),\
#                     ('Ana', 'up20186040', (90, 90)),\
#                     ('José', 'up20186063', (70, 90)),\
#                     ('Ana', 'up20186061', (90, 90)),\
#                     ('Tiago', 'up20186070', (100, 90)))))

#print(sort_grades((('Maria', 'up20190001', (60, 70, 80)),\
#           ('Maria', 'up20190002', (60, 70, 80)),\
#           ('Mario', 'up20190003', (100, 10, 80)),\
#           ('Rui', 'up20190004', (90, 100, 90)),\
#           ('Ana', 'up20190005', (90, 100, 90)))\
#))
