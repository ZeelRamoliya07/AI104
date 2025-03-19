# Pangrams

import string

s = input()
s = s.lower()

s = list(s)
li = []

for i in range(len(s)):
    if s[i].isalpha():
        li.append(s[i])
        
li = list(set(li))
print(li)

if len(li) == 26:
    print("panagram")
else:
    print("not panagram")