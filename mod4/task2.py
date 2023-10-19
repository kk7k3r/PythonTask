def pow(num, degree ):
    if (num == 0):
        return 1
    if (num % 2 == 0):
        return (num  ** 2) ** (degree/2)
    else: return num * num **(degree - 1)


a = int(input())
n = int(input())
print(pow(a, n))