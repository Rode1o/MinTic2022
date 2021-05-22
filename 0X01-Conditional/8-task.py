import math
x = int(input())
if x > 99 and x < 1000:
    pos0 = x // 100
    dig = math.log10(x) + 1
    pos1 = int(x // math.pow(10, dig // 2)) % 10
    pos2 = x % 10
    if pos0 > pos1 and pos0 > pos2:
        print("pos0 >")
    elif pos1 > pos0 and pos1 > pos0:
        print("pos1 >")
    elif pos2 > pos0 and pos2 > pos1:
        print("pos 2 >")
    else:
        print("invalid")
else:
    print("invalid")