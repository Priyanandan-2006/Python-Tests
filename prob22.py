a = input()

count = 0

for b in range(len(a) - 1):
    if int(a[b:b+2]) % 2 != 0:
        count = count + 1

print(count)