s = 'abcdefghijklmnopqrstuvwxyz'
result = s[0]
temp = s[0]

for num in range(0, len(s) - 1):
    if s[num] <= s[num + 1]:
        temp += s[num + 1]

        if len(temp) > len(result):
            result = temp
    else:
        temp = s[num + 1]

print('Longest substring in alphabetical order is: ' + result)