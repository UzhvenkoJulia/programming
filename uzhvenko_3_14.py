import math

n = int(input())
factorial = math.factorial(n)
digits_count = int(math.log10(factorial)) + 1

print(digits_count)