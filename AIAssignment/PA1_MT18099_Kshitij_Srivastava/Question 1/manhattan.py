def calcManhattan(test, n):
    # test = [1,n,4,7,8,6,2,0,5]
    # goal = [0,1,2,3,4,5,6,7,8]
    ind = test.index(0)
    sum = 0
    for i in range(n**2):
            sum += abs(int(i / n) - int(test[i] / n)) + abs(i % n - test[i] % n)
    sum -= abs(int(ind / n) - int(test[ind] / n)) + abs(ind % n - test[ind] % n)
    return sum