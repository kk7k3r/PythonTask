path = input()
f = open(path).readlines()
dict = {}
for i in range(len(f)):
    for j in range(len(f[i])):
        if not (f[i][j].isalpha()):
            continue
        if (dict.get(f[i][j].lower()) == None):
            dict[f[i][j].lower()] = 1
        else: dict[f[i][j].lower()] += 1
print(sorted(dict.items(), key=lambda item: item[1], reverse=True))