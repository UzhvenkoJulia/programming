def add(n):
    t = n % 10
    if n == 0:
        return 0
    return t * (1 + t) // 2 + n // 10 * 45 + add(n // 10)


def c_sum(p, q):
    return add(q) - add(p - 1)


while True:
    p, q = map(int, input().split())
    if p + q < 0:
        break
    print(c_sum(p, q))