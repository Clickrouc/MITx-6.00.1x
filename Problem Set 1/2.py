# Problem 2

# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

s = 'bobboboobofxbob'
substr = 'bob'
result = 0

for num in range(len(s) - len(substr) + 1):
    print(s[num:len(substr)+num])
    if (s[num:len(substr)+num] == substr):
        result += 1

print('Number of times bob occurs is: ' + str(result))