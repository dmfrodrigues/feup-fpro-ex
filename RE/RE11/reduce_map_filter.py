from functools import reduce
def reduce_map_filter(args):
    if type(args) == list:
        return list(args)
    elif type(args) == tuple:
        l = list(reduce_map_filter(args[2]))
        if args[0] == "map":
            return list(map(args[1], l))
        elif args[0] == "filter":
            return list(filter(args[1], l))
        elif args[0] == "reduce":
            return reduce(args[1], l)

print(reduce_map_filter(('reduce', lambda a,b: a+b, ('map', lambda x: 2*x, ('filter', lambda x: x%2 != 0, [1,2,3])))))
