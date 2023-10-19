def get_message(nums):
    a = set()
    for i in range(len(nums)):
        a.add(nums[i])
    if (len(a) == 1):
        return "Все числа равны"
    elif (len(a) == len(nums)):
        return "Все числа разные"
    else: return "Есть равные и неравные числа"
    
user_input = list(map(int, input().split()))
print(get_message(user_input))
