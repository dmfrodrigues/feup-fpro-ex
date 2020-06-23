def totalsum(wishlist, products):
    ret = 0
    for s in wishlist.keys():
        ret += wishlist[s]*products[s]
    return ret

def budgeting(budget, products, wishlist):
    pricing = [];
    for s in products.keys():
        pricing.append((products[s], s));
    pricing = sorted(pricing);
    #print(pricing);
    while totalsum(wishlist, products) > budget:
        for i in range(len(pricing)):
            if pricing[i][1] in wishlist:
                wishlist[pricing[i][1]] -= 1;
                if wishlist[pricing[i][1]] <= 0:
                    del wishlist[pricing[i][1]];
                break;
    return wishlist

print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40, 'pc': 600, 'glasses': 75},\
                      {'ps4': 1, 'smartphone': 1, 'pc': 1}))
print(budgeting(1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100},\
                      {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox':1}))
print(budgeting(1200, {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100},\
                      {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox':1}))
