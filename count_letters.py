def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] +=1
    return result

print(count_letters("aaaaa"))
print(count_letters("tenant"))
print(count_letters("loong string with a lot of letters"))