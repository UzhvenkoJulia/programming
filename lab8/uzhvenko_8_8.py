n = int(input(" "))
r = ""

while n > 0:
    if n % 2 == 1:
        r = "SX" + r
    else:
        r = "S" + r
    n //= 2


r = r[2:]

print(" ", r)

