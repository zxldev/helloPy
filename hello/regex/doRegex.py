import re

print(re.match(r'^\d+$','3155a'))
print(re.split(r'[\s,]+','a b ,, c ,d'))
match = re.match(r'^\d+([a-zA-z]+)\d+$','12312zxldev123123')
print(match.groups())
print(match.group(1))