import string

k = int(input())
p = input()

result = ""
for c in p:
    if c.isalpha():
        idx_c = string.ascii_lowercase.index(c.lower())
        idx_new = (idx_c + k) % 26
        c_new = string.ascii_lowercase[idx_new]
        result += c_new.upper() if c.isupper() else c_new
    else:
        result += c 

print(result)

