d = {'x': 10, 'y': 20}
print(d, type(d))
print(d['x'])


d['x'] = 100
print(d)
d['x'] = 'XXXXX'
print(d)


d['z'] = 200
print(d)
d[1] = 10000
print(d)


print(dict(a=10, b=20))
print(dict([('a', 10), ('b', 20)]))


d = {'x': 10, 'y': 20}
# print(help(d))
print(d.keys())
print(d.values())
d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)


print(d['x'])
print(d.get('x'))
# print(d['z'])  # KeyError: 'z'
print(d.get('z'))  # None
print(type(d.get('z')))  # <class 'NoneType'>


print(d.pop('x'))
print(d)
del d['y']
print(d)
del d
# print(d)  # NameError: name 'd' is not defined
d = {'a': 10, 'b': 20, 'c': 30}
d.clear()  # 空にする
print(d)  # {}


d = {'a': 10, 'b': 20, 'c': 30}
print('a' in d)
print('j' in d)


x = {'a': 1}
y = x  # dict -> call by reference
y['a'] = 1000
print(x)
print(y)


x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)


# dict -> hash table: 検索が早い（<-> listに入れて検索すると遅い/先頭から探すため）
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}
print(fruits['apple'])
