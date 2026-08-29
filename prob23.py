a = input()

count = 0

for b in a:
    if int(b) == 1 or int(b) == 4 or int(b) == 9:
        count = count + 1

print(count)
