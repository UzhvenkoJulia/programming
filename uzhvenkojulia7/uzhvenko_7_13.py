def has_unique_digits(num):
    num_str = str(num)
    return len(set(num_str)) == len(num_str)
def generate_numbers_with_unique_digits(a, b):
    result = []
    for num in range(a, b + 1):
        if has_unique_digits(num):
            result.append(num)
    return result
a, b = map(int, input().split())
result = generate_numbers_with_unique_digits(a, b)
print(*result, sep=' ')