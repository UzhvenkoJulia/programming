n = int(input())
result = 0
if n == 1:
    for i in range(100, 1000):
        if i % 2 == 0:
            result += i
elif n == 2:
    for i in range(100, 1000):
        digits = [int(digit) for digit in str(i)]
        if digits[0] < digits[1] < digits[2]:
            result += 1
elif n == 3:
    for i in range(100, 1000):
        digits = [int(digit) for digit in str(i)]
        if digits[0] % 2 != 0 and digits[1] % 2 != 0 and digits[2] % 2 != 0:
            result += i
elif n == 4:
    for i in range(100, 1000):
        digits = [int(digit) for digit in str(i)]
        if digits[0] > digits[1] > digits[2]:
            result += 1
elif n == 5:
    for i in range(100, 1000):
        digits = [int(digit) for digit in str(i)]
        if i == sum([digit ** 3 for digit in digits]):
            result += i
elif n == 6:
    for i in range(100, 1000):
        digits = set([int(digit) for digit in str(i)])
        if len(digits) == 3:
            result += 1
print(result)