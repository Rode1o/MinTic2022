x = int(input())
count = 0
a = 2
if x > 10 and x < 21:
    while (a <= x//2):
        if (x % a == 0):
            count += 1
            break
        a += 1

    if (count ==0 and x != 1):
        print("Prime")
    else:
        print("Isnt Prime")
else:
    print("invalid")