#coding:utf-8

N = int(raw_input())
s = list(raw_input())
K = int(raw_input()) % 26

for i, char in enumerate(s):
    if char >= 'A' and char <= 'Z':
        num = ord(char) + K
        if num > 90:
            num -= 26 
    elif char >= 'a' and char <= 'z':
        num = ord(char) + K
        if num > 122:
            num -= 26
    else:
        continue
    s[i] = chr(num)

print ''.join(s)


