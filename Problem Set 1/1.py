# Problem 1

# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

s = 'azcbobobegghakl'
wovels = 'aeiou'
result = 0

for char in s:
    for wovel in wovels:
        if char == wovel:
            result += 1

print('Number of vowels: ' + str(result))