k = int(input())
n = int(input())
decimal_number = 0
power = 0
while n > 0:
    digit = n % 10
    decimal_number += digit * (k ** power)
    n //= 10
    power += 1
print(decimal_number)