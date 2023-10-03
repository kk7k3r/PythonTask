str = input()
res = ""
previous_symb = ""
for i in range(len(str)):
    if (str[i] == " "):
        res += previous_symb
    if (i == len(str) - 1):
        res += str[i]
    previous_symb = str[i]
print(res)
    
