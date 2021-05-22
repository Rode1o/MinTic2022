import math
x = int(input())
if x > 99 and x < 1000:
    pos0 = x // 100
    dig = math.log10(x) + 1
    pos1 = int(x // math.pow(10, dig // 2)) % 10
    pos2 = x % 10
    if pos0 % pos1 == 0 or pos0 % pos2 == 0 or pos1 % pos2 == 0 \
       or pos1 % pos0 == 0 or pos2 % pos0 == 0 or pos2 % pos1 == 0:
        print("Multipler")
    else:
        print("invalid")
else:
    print("invalid")