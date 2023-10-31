s = input()
word = [char for char in s if char.isalnum]
print(word[2] + word[6] + word[10])  
print(word[0] + word[len(word) - 2] + word[len(word) - 1])  
print(s[0:7])  
print(s[4:])  
odd_chop = s[1:len(s):2]
print(odd_chop)  
print(len(odd_chop))  
print(s[::-1])