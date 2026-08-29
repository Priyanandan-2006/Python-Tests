a = input()

count = 0

for b in a:
    if int(b) in [2, 3, 5, 7]:
        count = count + 1

print(count)