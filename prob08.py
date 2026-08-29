for a in range(10, 100):
    if a % 2 == 0 and a // 10 + a % 10 == 6:
        print(a)