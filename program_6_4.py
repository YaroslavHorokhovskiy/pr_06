"""Task #4: Write a Python function to reverses a string if its length
is a multiple of 4.
"""
def get_modified_str(s: str) -> str:
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s

s = input('Введіть будь-яку послідовність символів: ')
print(f'Модіфікована послідовність символів: {get_modified_str(s)}')
