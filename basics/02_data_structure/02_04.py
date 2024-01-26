x = {1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8}
print(x, type(x))


a = {1, 2, 3, 4, 5, 6}
b = {2, 3, 3, 6, 7}
print(a - b)  # 差集合
print(a | b)  # 和集合
print(a & b)  # 積集合
print(a ^ b)  # 排他的論理和集合


s = {1, 2, 3, 4, 5}
# s[0]  # TypeError: 'set' object is not subscriptable
s.add(6)
print(s)
s.add(6)
print(s)


s.remove(6)
print(s)
s.clear()
print(s)


my_friends = {'A', 'B', 'D'}
her_friends = {'B', 'D', 'E', 'F'}
print(my_friends & her_friends)


f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)  # 種類を知りたい -> 重複を取り除く
print(kind)
