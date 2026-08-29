a = int(input())

count = 0

while a > 0:
    if a % 10 % 2 != 0:
        count = count + 1
    a = a // 10

print(count)