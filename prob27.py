count = 0

for a in range(100000):
    b = a
    sum = 0

    while b > 0:
        sum = sum + b % 10
        b = b // 10

    if sum == 14:
        count = count + 1

print(count)
