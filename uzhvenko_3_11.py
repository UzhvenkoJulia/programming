n = int(input())
summ = 0
while n > 0:
    last = n % 10
    n = n // 10
    if last % 2 == 0:
        summ += last
print(summ)