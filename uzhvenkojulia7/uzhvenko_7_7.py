def nsd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def nsk(a, b):
    return a * b // nsd(a, b)
def found_nsk_to_n(n):
    nsk_to_n = 1
    for i in range(2, n + 1):
        nsk_to_n = nsk(nsk_to_n, i)
    return nsk_to_n
n = int(input())
print(found_nsk_to_n(n))