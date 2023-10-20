def get_count_symbols(word):
    dict = {}
    for i in range(len(word)):
        if (dict.get(word[i].lower()) == None):
            dict[word[i]] = 1
        else: 
            dict[word[i]]+= 1
    return dict

def make_palindrome(word):
    temp = 0
    left = ""
    right = ""
    mid = ""
    for (a, b) in get_count_symbols(user_input).items():
        if b % 2 != 0:
            if temp != 0:
                return "No"
            else:
                temp += 1
                mid = a * b
        else:
            left += a * (b // 2)
            right = a * (b // 2) + right
    return left + mid + right

user_input = input()
print(make_palindrome(user_input))

            