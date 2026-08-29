a=int(input())
if a % 10 + (a // 100) < 10:
    print("Success")
else:
    print("Failure")