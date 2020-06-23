def sort_by_f(l):
    return sorted(l, key=lambda x: 5-x if x>=5 else x)

print(sort_by_f([-10, -6, 2, 5, 90]))
