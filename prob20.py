a = 0

for b in range(1, 10):
    count = 0

    for c in range(1, b + 1):
        if b % c == 0:
            count = count + 1

    if count == 2:
        a = a + 1

print(a)