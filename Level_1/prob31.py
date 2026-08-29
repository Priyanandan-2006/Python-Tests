a=int(input())
b=a // 100 + (a // 10) % 10 + a % 10
while b>=10:
    b=b // 10 + b % 10
print(b)