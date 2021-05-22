x = int(input())
if x > 9 and x < 100:
    x1 = (x // 10)
    x2 = (x % 10)
    if x1 != x2:
        print("Not")
    else:
        print("Equals")
else:
    print("Invalid")