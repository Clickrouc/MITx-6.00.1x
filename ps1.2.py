s = 'bobboboobofxbob'
substr = 'bob'
result = 0

for num in range(len(s) - len(substr) + 1):
    print(s[num:len(substr)+num])
    if (s[num:len(substr)+num] == substr):
        result += 1

print('Number of times bob occurs is: ' + str(result))