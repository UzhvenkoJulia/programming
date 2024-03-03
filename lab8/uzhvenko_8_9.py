n = int(input(""))   #1

result_b13 = ""


while n > 0:
    r = n % 13
    if r < 10:
        result_b13 = str(r) + result_b13
    else:
        result_b13 = chr(ord('A') + r - 10) + result_b13
    n //= 13


print(f"{result_b13}")


number = int(input())  #2

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

while number > 0:
    result = alphabet[number % 13] + result
    number //= 13


print(result)



