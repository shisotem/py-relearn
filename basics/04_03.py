"""
内包表記(Comprehension)
"""
t = (1, 2, 3, 4, 5)
l = [i for i in t]
print(l)

l = [i for i in t if i % 2 == 0]
print(l)

t2 = (5, 6, 7, 8, 9, 10)
# l = []
# for i in t:
#     for j in t2:
#         l.append(i * j)
l = [i * j for i in t for j in t2]
print(l)


w = ['Mon', 'Tue', 'Wed']
f = ['coffee', 'milk', 'water']
# d = {}
# for x, y in zip(w, f):
#     d[x] = y
# print(d)
d = {x: y for x, y in zip(w, f)}
print(d)


even_s = {i for i in range(10) if i % 2 == 0}
print(even_s)


def g():
    for i in range(5):
        yield i


g = g()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g = (i for i in range(5))
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

even_g = (i for i in range(5) if i % 2 == 0)
for i in even_g:
    print(i)


t = tuple(i for i in range(5))
print(type(t))
print(t)
