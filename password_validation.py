import re

pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}")
string = 'abcabcabc19$$'
check = pattern.fullmatch(string)

print(check)