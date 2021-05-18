def prnt(grid, n):
    for i in list(range(n)):
        for j in list(range(n)):
            print(grid[(i * n) + j], end=' ')
        print()