def sparse_dot_product(dict1, dict2):
    sum = 0
    for n in dict1:
        if n in dict2:
            sum += dict1[n] * dict2[n]
    return sum

print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1}))
print(sparse_dot_product({0: 1, 1: 1}, {2: 1, 3: 1}))
