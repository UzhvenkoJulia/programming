n = input()
updated_number = ""
for digit in n:
    digit = int(digit)
    if digit % 2 == 0:
        updated_number += str(digit + 1)
    else:
        updated_number += str(digit - 1)
print(updated_number)