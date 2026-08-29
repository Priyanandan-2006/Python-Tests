a=int(input())
b = a
count = 0

while b > 0:
    count = count + 1
    b = b // 10

first = a // (10 ** (count - 1))
last = a % 10
middle = (a % (10 ** (count - 1))) // 10

print(last * (10 ** (count - 1)) + middle * 10 + first)