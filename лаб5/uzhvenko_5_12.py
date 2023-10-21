n = int(input())
array = list(map(int, input().split()))

unique_elements = {}

i = 0
while i < n:
    element = array[i]
    if element not in unique_elements:
        unique_elements[element] = i
    i += 1
    
result = [array[index] for element, index in unique_elements.items()]
print(*result)