count = 0
# else: whileループ終了時に実行される
# ただし、break文でループを抜けた場合は実行されない
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % count)


# while True:
#     word = input("Enter: ")
#     num = int(word)
#     if num == 100:
#         break
#     print("next")


# 'string': iterator
for c in 'string':
    print(c)


for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print("I ate all!")


for i in range(10):
    print(i)
for i in range(2, 10):
    print(i)
for i in range(2, 10, 3):
    print(i)


for _ in range(3):
    print("hello")


for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)


days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


d = {'x': 100, 'y': 200}
# key only
for k in d:
    print(k)


d = {'x': 100, 'y': 200}
print(d.items())  # dict_items([('x', 100), ('y', 200)])
for k, v in d.items():
    print(k, v)
