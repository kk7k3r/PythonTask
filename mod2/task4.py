def is_natural_num(str):
    return str.isdigit() & int(str) >= 0

def get_bin(num):
    res = ""
    while(num != 0):
        res += str(num % 2)
        num //= 2
    return res[::-1]

def get_oct(num):
    res = ""
    while(num != 0):
        res += str(num % 8)
        num //= 8
    return res[::-1]

def get_hex(num):
    res = ""
    while(num != 0):
        res += str(num % 16)
        num //= 16
    return res[::-1]

a = input()
if (is_natural_num(a)):
    num = int(a)
    print(get_bin(num), get_oct(num), get_hex(num))
else:
    print("Неверный ввод")

