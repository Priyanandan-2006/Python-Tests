a = int(input())
count = 0
sum = 0
b = a
for c in range(1, a + 1):
    if a % c == 0:
        count = count + 1

while b > 0:
    sum = sum + b % 10
    b = b // 10

if count == 2 and sum == 14:
    print("Prime & Sum of Digits is 14")
elif count != 2 and sum == 14:
    print("Not Prime but sum of digits is 14")
elif count == 2 and sum != 14:
    print("Prime, but sum of Digits is not 14")