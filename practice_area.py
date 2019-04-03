def common_letters(string_one, string_two):
    common =[]
    for letter in string_one:
        for character in string_two:
            if letter == character:
                common.append(letter)
    return common

print(common_letters("banana", "cream"))