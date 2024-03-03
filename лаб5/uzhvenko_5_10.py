n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))

elements_first = set(first)
elements_second = set(second)

result = []
for num in first:
    if num not in elements_second:
        result.append(num)

print(len(result))
print(*result)