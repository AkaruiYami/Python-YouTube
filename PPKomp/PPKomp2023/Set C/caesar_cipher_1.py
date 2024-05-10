import string
k = int(input())
p = input()

chars = set()
for _p in p:
    _p = _p.lower()
    if _p in string.ascii_lowercase:
        chars.add(_p)

translate_table = {}
ord_a = ord("a")
for c in chars:
    c_ord = ord(c)
    char_id = c_ord - ord_a
    new_char_id = (char_id + k) % 26
    new_c = chr(ord_a + new_char_id)

    translate_table[c_ord] = ord(new_c)
    translate_table[ord(c.upper())] = ord(new_c.upper())


p = p.translate(translate_table)
print(p)

