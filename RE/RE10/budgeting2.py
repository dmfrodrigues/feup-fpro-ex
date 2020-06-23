def expand(products, cost):
    ret = []
    for i in products.keys():
        for _ in range(products[i]):
            ret.append((i,cost[i]))
    return ret

def best(lhs, rhs, cost):
    if lhs == None:
        return rhs
    if rhs == None:
        return lhs

    W1 = 0
    for s in lhs:
        W1 += cost[s]
    W2 = 0
    for s in rhs:
        W2 += cost[s]
    if W1 > W2 or (W1 == W2 and len(lhs) <= len(rhs)):
        return lhs
    else:
        return rhs

def knapsack(B, products, cost):
    if len(products) <= 0:
        return []

    opt1 = knapsack(B, products[1:], cost)
    if B-products[0][1] >= 0:
        opt2 = [products[0][0]] + knapsack(B-products[0][1], products[1:], cost)
    else:
        opt2 = None
    return best(opt1, opt2, cost)

def budgeting2(budget, products, wishlist):
    lst = expand(wishlist, products)
    l = knapsack(budget, lst, products)
    ret = dict()
    for s in l:
        if s not in ret:
            ret[s] = 0
        ret[s] += 1
    return ret

print(budgeting2 (1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40,\
                         'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))
print(budgeting2 (1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50,\
                         'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox': 1}))
print(budgeting2 (1000, {'laptop': 2000, 'jeans': 50}, {'laptop': 2,'jeans': 3}))
