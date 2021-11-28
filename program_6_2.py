"""Task #2: Write a Python program to get a string made of the first 2 and
the last 2 chars from a given a string. If the string length is less than 2,
return instead the empty string.

Sample Strings:
    'w3resource' Expected Result: 'w3ce'
    'w3' Expected Result: 'w3w3'
    'w' Expected Result: Empty String
"""
def get_modified_str(s: str) -> str:
    if len(s) < 2:
        return ''

    return s[: 2] + s[-2: ]

s1 = 'w3resource'
s2 = 'w3'
s3 = 'w'

print(f'Input: {s1}')
print(f'Output: {get_modified_str(s1)}')

print(f'\nInput: {s2}')
print(f'Output: {get_modified_str(s2)}')

print(f'\nInput: {s3}')
print(f'Output: {get_modified_str(s3)}')
