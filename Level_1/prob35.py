a = int(input())
b = int(input())

if a % 10 + a // 100 > b % 10 + b // 100:
    print(a % 10 + (a // 10) % 10 + a // 100)
else:
    print(b % 10 + (b // 10) % 10 + b // 100)