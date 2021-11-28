"""Task #5: Write a Python program that accepts a comma separated sequence of
words as input and prints the unique words in sorted form (alphanumerically).

Sample Words: red, white, black, red, green, black
Expected Result: black, green, red, white, red

"""
def get_unique_words(s: str) -> list:
    return sorted(list(set([word.strip() for word in s.split(',')])))

s = input('Введіть довільну кількість слів, розділених комами: ')
print('Унікальні слова у відсортованому вигляді:')
print(', '.join(get_unique_words(s)))
