a = int(input())
matrix = [[x for x in range(1, a + 1)] for y in range(a)]
res = [[matrix[j][i] for j in range(a)] for i in range(a)]

for i in range(a):
    print(*matrix[i], sep= ", ")
print()
for i in range(a):
    print(*res[i], sep= ", ")