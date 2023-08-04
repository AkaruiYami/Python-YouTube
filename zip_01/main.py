import itertools

a = [1, 2, 3]
b = ("a", "b", "c", "d", "e")

z1 = zip(a, b)
print(z1)

z1 = list(z1)
print(z1)

# include the extra elements
z2 = list(itertools.zip_longest(b, a, fillvalue="Saya Hilang"))
print(z2)


# transpose a matrix
m_1 = [[1, 2], [3, 4], [5, 6]]
t_m_1 = list(zip(*m_1))
t_m_2 = list(zip(m_1[0], m_1[1], m_1[2]))

print(t_m_1)
print(t_m_2)
