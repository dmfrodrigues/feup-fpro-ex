def fight(heroes, villain):
    for h in heroes:
        if h["category"] != villain["category"]:
            continue
        if h["health"] >= villain["health"]:
            return "%s defeated the villain and now has a score of %d"%(h["name"], h["score"]+1)
        else:
            villain["health"] -= h["health"]/2
    return "%s prevailed with %.1fHP left"%(villain["name"], villain["health"])

print(fight([{'name': 'Genos', 'health': 3000, 'category': 'S', 'score': 0},\
             {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0},\
             {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0},\
             {'name': 'King', 'health': 3750, 'category': 'S', 'score': 1}],\
             {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}))