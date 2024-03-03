n = int(input())
array = list(map(int, input().split()))

temp = array[-1]

i = n - 1
while i > 0:
    array[i] = array[i - 1]
    i -= 1

array[0] = temp

print(*array)