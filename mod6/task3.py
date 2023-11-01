def generator_armstrong_numbers():
    counter = 10
    yield 1
    while(True):
        counter += 1
        str_num = str(counter)
        num = 0
        for i in range(len(str_num)):
            num += int(str_num[i]) ** len(str_num)
        if (num == counter):
            yield counter

generator = generator_armstrong_numbers()

def get_armstrong_numbers():
    return next(generator)

for i in range(8):
    print(get_armstrong_numbers(), end=' ')

# Ожидаемый результат кода:
# 1 153 370 407 1634 8208 9474 54748 
