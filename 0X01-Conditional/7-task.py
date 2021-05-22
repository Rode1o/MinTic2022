x = int(input())
y = int(input())

if x > 9 and x < 100:
    if y > 9 and y < 100:
        x1 = (x // 10)
        x2 = (x % 10)
        y1 = (x // 10)
        y2 = (x % 10)
        print (x1+x2+y1+y2)
    else:
        print("invalid")
else:
    print("invalid")