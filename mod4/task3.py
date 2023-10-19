def search(num1, num2):
    if (num1 == 0):
        return num2
    if (num2 == 0):
        return num1
    if (num1 > num2):
        return search(num1 % num2, num2)
    else:
        return search(num1, num2 % num1)
    
n1 = int(input())
n2 = int(input())
print(search(n1, n2))