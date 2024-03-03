def digit_to_char(digit):
    if 0 <= digit <= 9:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)

def char_to_digit(char):
    if char.isdigit():
        return int(char)
    else:
        return ord(char) - ord('A') + 10

def from_base_m_to_decimal(number, base_m):
    decimal_number = 0
    power = 0
    for digit in reversed(number):
        decimal_number += char_to_digit(digit) * (base_m ** power)
        power += 1
    return decimal_number

def from_decimal_to_base_k(decimal_number, base_k):
    if decimal_number == 0:
        return '0'
    converted_number = ''
    while decimal_number > 0:
        remainder = decimal_number % base_k
        converted_number = digit_to_char(remainder) + converted_number
        decimal_number //= base_k
    return converted_number


m, k = map(int, input().split())
number_in_m_base = input().strip()
decimal_number = from_base_m_to_decimal(number_in_m_base, m)
result = from_decimal_to_base_k(decimal_number, k)
print(result.lstrip('0') or '0')