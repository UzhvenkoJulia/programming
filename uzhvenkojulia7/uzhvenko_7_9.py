def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def is_lucky_prime(num):
    return is_prime(num) and is_prime(int(str(num)[::-1])) and num != int(str(num)[::-1])
def find_lucky_prime(K):
    count = 0
    num = 2
    while True:
        if is_lucky_prime(num):
            count += 1
            if count == K:
                return num
        num += 1
    return -1
K = int(input())
result = find_lucky_prime(K)
print(result)