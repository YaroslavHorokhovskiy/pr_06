"""Task #3: Write a Python program to get a string from a given string
where all occurrences of its first char have been changed to '$' except
the first char itself.

Sample String: 'restart' Expected Result: 'resta$t
"""
def get_modified_str(s: str) -> str:
    return s[0] + s[1:].replace(s[0], '$')

    # Інше рішення:
    # new_s = s[0]
    # for i in range(1, len(s)):
    #     if s[i] == s[0]:
    #         new_s += '$'
    #     else:
    #         new_s += s[i]
    # return new_s

s = input('Введіть будь-яку послідовність символів: ')
print(f'Модіфікована послідовність символів: {get_modified_str(s)}')
