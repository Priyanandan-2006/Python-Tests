a = input()

count = 0

for b in range(len(a) - 1):
    if int(a[b:b+2]) in [16, 25, 36, 49, 64, 81]:
        count = count + 1

print(count)