factorial_result = int(input())
n = 1
factorial = 1
while factorial < factorial_result:
    n += 1
    factorial *= n
if factorial == factorial_result:
    print(n)
else:
    print("Введене значення не відповідає жодному n!")