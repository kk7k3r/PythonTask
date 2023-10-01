wrong_message = "Неверный ввод"
try:
    a = int(input())
    if(a < 0):
        print(wrong_message)
    else:
        print(bin(a)[2:], oct(a)[2:], hex(a)[2:])
except:
    print(wrong_message)

