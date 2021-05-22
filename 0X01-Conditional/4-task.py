x = int(input())
count = 0
a = 2
if x > 9 and x < 100 or x > -99 and x < -9:
    if x < 0:
        print("negative")
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