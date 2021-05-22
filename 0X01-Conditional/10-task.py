x = int(input())
y = int(input())
z = int(input())


if (x > 9 and x < 100) and (y > 9 and y < 100) \
    and(z > 9 and z < 100):
    x1 = (x // 10)
    x2 = (x % 10)
    y1 = (y // 10)
    y2 = (y % 10)
    z1 = (z // 10)
    z2 = (z % 10)
    bigger = [x1, x2, y1, y2, z1, z2]
    bigger_s = sorted(bigger)
    print(bigger_s[5])
    
else:
    print("invalid")
    
