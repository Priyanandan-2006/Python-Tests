a = int(input())

b = a

while b >= 10:
    b = b // 10

if b % 2 == 0:
    print(a)
else:
    print((b - 1) * 10 ** (len(str(a)) - 1) + a % 10 ** (len(str(a)) - 1))