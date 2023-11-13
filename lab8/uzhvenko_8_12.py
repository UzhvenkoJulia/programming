something = 1

while True:
    i, j, k = map(int, input().split())
    if i + j + k == 0:
        break

    u = 10 ** k

    res = pow(i % u, j, u)


    print("Case #{}: {}".format(something, res))
    something += 1
    
    
    