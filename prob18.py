a = int(input())

b = a % 100
count = 0

for c in range(1, b + 1):
    if b % c == 0:
        count = count + 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")