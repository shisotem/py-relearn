t = (1, 2, 3, 4, 5, 2)
print(type(t))
# t[0] = 4  # TypeError: 'tuple' object does not support item assignment


lt = ([1, 2], [3, 4])
# lt[0] = [5, 6]  # TypeError: 'tuple' object does not support item assignment
lt[0][0] = 5  # Ok
print(lt)


print(t[-2])
print(t[1:3])  # (2, 3)
print(t.index(2))
print(t.index(2, 2))
print(t.count(2))


t = 1, 2, 3
print(t, type(t))
# t = 1,
# print(t, type(t))  # (1,) <class 'tuple'>


t = ()
print(t, type(t))


# t = (1)
# print(t, type(t))  # 1 <class 'int'>
t = (1,)
print(t, type(t))  # (1,) <class 'tuple'>


new_t = (1,) + (4, 5, 6)
print(new_t)


# unpacking
num_t = (10, 20)
x, y = num_t
print(x, y)
x, y = 10, 20
print(x, y)


# swap
i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)


a = 10
b = 20
a, b = b, a
print(a, b)


choose_two_from_three = ('A', 'B', 'C')
answer = []
answer.append('A')
answer.append('C')
print(answer)
