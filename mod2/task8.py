s = input()
i = input()

count = 0
while(len(s) != count):
    if (s[count] == i):
        count += 1
    else:
        break
print(count)