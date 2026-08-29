a = int(input())
b = int(input())

if (a // 10) % 10 > (b // 10) % 10:
    print(abs(a % 10 - a // 100))
else:
    print(abs(b % 10 - b // 100))