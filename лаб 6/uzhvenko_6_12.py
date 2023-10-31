def decrypt_caesar_cipher(encryption, k):
    d_text = ""
    for char in encryption:
        if char.isalpha():
            c_code = ord(char)
            is_upper = char.isupper()
            c_code -= k
            if is_upper and c_code < ord('A'):
                c_code += 26
            elif not is_upper and c_code < ord('a'):
                c_code += 26
            decrypted_char = chr(c_code)
            d_text += decrypted_char
        else:
            d_text += char
    return d_text
encryption = input()
k = int(input())
d_text = decrypt_caesar_cipher(encryption, k)
print(d_text)