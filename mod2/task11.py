def same_numbers(str):
    temp = ""
    for i in range(len(str)):
        if (not str[i].isdigit()):
            continue;
        if (str[i] in temp):
            return True
        temp += str[i];
    return False
    

str = input()
print(same_numbers(str))
