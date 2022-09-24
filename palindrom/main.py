def palindrom(string: str):
    s = string.replace(' ', '')
    return s == s[::-1]

print(palindrom('abcd'))
print(palindrom('taco cat'))
print(palindrom('black cat'))
print(palindrom('rotator'))
