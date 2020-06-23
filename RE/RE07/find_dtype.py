def find_dtype(atuple, data_type):
    ret = []
    for obj in atuple:
        if type(obj) == eval(data_type):
            ret.append(obj)
    return tuple(ret)

#print(find_dtype((1,False,"hello",2.,"world"), "str"))
#print(find_dtype((1,2,3), "float"))

