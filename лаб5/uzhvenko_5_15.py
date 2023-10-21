n = int(input())
num = list(map(int, input().split()))
x_element = max(num)
n_element = min(num)
for i in range(n):
    if num[i] == x_element:
        num[i] = n_element
    elif num[i] == n_element:
        num[i] = x_element
print(*num)