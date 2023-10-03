a = input()
odd_sum = 0
uneven_sum = 0
for i in range(len(a)):
    if (i % 2 == 1):
        odd_sum+= int(a[i])
    else:
        uneven_sum += int(a[i])
print(odd_sum * 3)
print(uneven_sum)
if ((uneven_sum + 3 * odd_sum) % 10 == 0):
    print("Yes")
else:
    print("No")