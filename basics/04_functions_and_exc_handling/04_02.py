import time


# 関数内関数: 関数内でのみ繰り返す処理がある場合
def outer(a, b):
    def plus(c, d):
        return c + d

    print(plus(a, b))


outer(1, 2)


# このような時の関数内関数innerをclosureという
# 変数のbinding: a, bの状態が、関数内関数でも保持されている
def outer(a, b):
    def inner():
        return a + b

    return inner


f = outer(1, 2)
# <function outer.<locals>.inner at 0x10422c4a0>
# innerはouterのローカルスコープ内で定義された関数という意味
print(f)
print(f())


# e.g. circle_area closes over pi
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


calc1 = circle_area_func(3.14)
calc2 = circle_area_func(3.1415926535)
print(calc1(10))
print(calc2(10))


"""
おまけ:
Pythonでは、関数内部から外部スコープの変数を直接"変更"することはできません
（ただし、その変数が可変型（リストや辞書など）の場合は例外です）。
この問題を解決するためには、nonlocalキーワードを使用して、
numが外部スコープの変数であることをPythonに伝える必要があります。
nonlocal文は、列挙された識別子が
グローバルを除く一つ外側のスコープで先に束縛された変数を参照するようにします。
"""


def increment_outer(num):
    def increment_inner():
        nonlocal num  # Pythonの場合これが必要
        print(num)
        num += 1  # 変更時のUnboundLocalErrorを防ぐためには...

    return increment_inner


f = increment_outer(100)
f()  # 100
f()  # 101
f()  # 102


# decorator
def print_info(func):
    def wrapper(*args, **kwargs):  # 任意の引数
        print('start')
        result = func(*args, **kwargs)  # unpacking
        print('end')
        return result

    return wrapper


def add_num(a, b):
    return a + b


f = print_info(add_num)
print(f(10, 20))


@print_info
def add_num(a, b):
    return a + b


print(add_num(10, 20))


def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result

    return wrapper


# 順序も重要: f = print_info(print_more(add_num))
@print_info
@print_more
def add_num(a, b):
    return a + b


# 実行順序とreturn resultの連鎖が、≈stack/recursiveな感じ
# info -> more -> add_num -> more -> info
print(add_num(10, 20))
# start
# func: add_num
# args: (10, 20)
# kwargs: {}
# result: 30
# end
# 30


l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word), end=' ')
    print()


# def sample_func(word):
#     return word.capitalize()

# change_words(l, sample_func)


sample_func = lambda word: word.capitalize()
change_words(l, sample_func)


# 引数に関数を渡す場合にlambdaは特に便利
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())


# iterator(e.g. list, dict): 予め全要素をメモリに格納する -> forで順に取り出す
# generator: 要素が必要になるたびに生成

l = ['Good morning', 'Good afternoon', 'Good night']
for i in l:
    print(i)


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


for g in greeting():
    print(g)


g = greeting()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # StopIteration


# 重い処理をgeneratorで小分けにする
def greeting():
    yield 'Good morning'  # 1

    time.sleep(2)  # 2
    print('Completed heavy tasks!')  # 2
    yield 'Good afternoon'  # 2

    time.sleep(2)  # 3
    print('Completed heavy tasks!')  # 3
    yield 'Good night'  # 3


g = greeting()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
