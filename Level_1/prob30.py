a=int(input())
if (a // 10) % 10+(a // 100)%10 == 10 and ((a // 10)%10>7 or (a // 100)%10>7):
    print("Success")
else:
    print("Failure")