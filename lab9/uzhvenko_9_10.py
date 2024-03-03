def count_unique_contacts(N, ph_numbers):
    unique_contacts = set(ph_numbers)
    return len(unique_contacts)

N = int(input())
ph_numbers = input().split()

result = count_unique_contacts(N, ph_numbers)
print(result)