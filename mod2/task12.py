a = input()
res = ""
for i in range(len(a)):
    if(a[i].isdigit() or a[i] == "+"):
        res += a[i]
print(res)