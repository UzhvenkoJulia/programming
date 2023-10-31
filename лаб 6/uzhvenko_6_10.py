input_string = input()
doubled_l = ''
for char in input_string:
    if char.isalpha():
        doubled_l += char * 2
    else:
        doubled_l += char
print(doubled_l)