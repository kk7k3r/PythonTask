a = input()
res = ""
domen = ""
for i in range(len(a)):
    if (a[i] == '.'):
        res = f"{domen}\n{res}"
        domen = ''
    elif (i == len(a) - 1):
        domen += a[i]
        res = f"{domen}\n{res}"
    else:
        domen += a[i]
print(res)
