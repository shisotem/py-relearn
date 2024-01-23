l = [10, 20, 30, 40, 50]
print(l[-2])
print(l[2:])
# print(l[100])  # IndexError: list index out of range


n = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(n[::2])
print(n[::-1])


print(len(n))
print(type(n))
print(list('hello'))


x = [2, 'b']
print(x)


a = [10, 20, 30]
b = ['40', '50', '60']
c = [a, b]
print(c)
print(c[0][1])


s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s[0] = 'X'  # リストはミュータブル（<-> 文字列はイミュータブル）
print(s)
s[2:5] = ['C', 'D', 'E']
print(s)
s[2:5] = []
print(s)
s[:] = []
print(s)


n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n.append(100)
print(n)
n.insert(0, 200)
print(n)
n.pop()
print(n)
n.pop(0)
print(n)


del n[0]
print(n)
del n


m = [1, 2, 2, 3, 3]
m.remove(2)
print(m)
m.remove(2)
# m.remove(2)  # ValueError: list.remove(x): x not in list


a = [1, 2, 3]
b = [4, 5, 6]
x = a + b
print(x)
a += b
print(a)
a.extend(b)
print(a)


r = [0, 1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 4))
print(r.count(3))
if 5 in r:
    print('exist')
r.sort()  # 破壊的メソッド
print(r)
r.sort(reverse=True)
print(r)
r.sort()
print(r)
r.reverse()
print(r)


s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)
x = '-'.join(to_split)
print(x)


# print(help(list))  # メソッド一覧を確認可能


i = [1, 2, 3, 4, 5]
j = i  # list, dict -> call by reference
j[0] = 100
print('j = ', j)
print('i = ', i)


x = [1, 2, 3, 4, 5]
y = x.copy()  # y = x[:] でも同じ
y[0] = 100
print('y = ', y)
print('x = ', x)


x = 20
y = x
y = 5
print(f'x: {x}, {id(x)}')
print(f'y: {y}, {id(y)}')


x = ['a', 'b']
y = x
y[0] = 'p'
print(f'x: {x}, {id(x)}')
print(f'y: {y}, {id(y)}')


seat = []
min = 0
max = 5
print(min <= len(seat) < max)
seat.append('p')
print(min <= len(seat) < max)
seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')
print(min <= len(seat) < max)
print(seat.pop(0))
print(min <= len(seat) < max)
