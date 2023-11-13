n = int(input())   

num = list(range(1, n + 1))

while True:
    print(*num)
    a = n - 2
    
    while a >= 0 and num[a] > num[a + 1]:
        a -= 1
    if a == -1:
        break
    k = n - 1
    
    while num[k] < num[a]:
        k -= 1
        
        
    num[a], num[k] = num[k], num[a]
    num[a + 1:] = reversed(num[a + 1:])
    
    
    