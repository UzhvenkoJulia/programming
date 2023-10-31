password = input()
categories_count = 0

# маленькі літери
if any(char.islower() for char in password):
    categories_count += 1

# великі літери
if any(char.isupper() for char in password):
    categories_count += 1

# цифри
if any(char.isdigit() for char in password):
    categories_count += 1

# символи
special_characters = "!\"#$%&'()*+"
if any(char in special_characters for char in password):
    categories_count += 1

if len(password) >= 8:
    categories_count += 1

print(categories_count)