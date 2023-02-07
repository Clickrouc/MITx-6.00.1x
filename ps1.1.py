s = 'azcbobobegghakl'
wovels = 'aeiou'
result = 0

for char in s:
    for wovel in wovels:
        if char == wovel:
            result += 1

print('Number of vowels: ' + str(result))