a = int(input())
b = int(input())
c = int(input())

d = max(a, b, c)

while True:
    if d % a == 0 and d % b == 0 and d % c == 0:
        print(d)
        break
    d = d + 1
    