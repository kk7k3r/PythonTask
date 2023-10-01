a = int(input())
b = int(input())
c = int(input())
if a > b:
    if (c > a):
        print(a)
    elif(c > b):
        print(c)
    else: print(b)
elif b > a:
    if (c > b):
        print(b)
    elif (c > a):
        print(c)
    else: print(a)
else: print(b)