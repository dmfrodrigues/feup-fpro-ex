def paint(n, boards):
    if n == 1:
        return max(boards)
    t = 0
    best = 1e9
    for i in range(len(boards)-n+1):
        t = max(t, boards[i])
        t_ = paint(n-1, boards[i+1:])
        best = min(best, t+t_)
    return best

print(paint(2,[60, 70, 10, 20, 40, 50, 10, 40]))
print(paint(3,[60, 70, 10, 20, 40, 50, 10, 40]))