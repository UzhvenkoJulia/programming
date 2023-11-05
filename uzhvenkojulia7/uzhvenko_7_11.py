def to_base_n(number, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number < base:
        return digits[number]
    else:
        return to_base_n(number // base, base) + digits[number % base]
def is_palindrome(number):
    return str(number) == str(number)[::-1]
def find_palindromic_bases(n):
    palindromic_bases = []
    for base in range(2, 37):
        num_in_base = to_base_n(n, base)
        if is_palindrome(num_in_base):
            palindromic_bases.append(base)
    return palindromic_bases

n = int(input())
palindromic_bases = find_palindromic_bases(n)
if len(palindromic_bases) == 0:
    print("none")
elif len(palindromic_bases) == 1:
    print("unique")
    print(palindromic_bases[0], end=" ")
else:
    print("multiple")
    print(*palindromic_bases, end=" ")