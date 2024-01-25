'''
say_something()  # NameError: name 'say_something' is not defined

def say_something():
    print('Hi')
'''


def say_something():
    print('Hi')


# 関数もfunctionクラスのインスタンス（function型のオブジェクト）
print(type(say_something))  # <class 'function'>
f = say_something
f()  # Hi


# あまり意味がない
def add_num(a: int, b: int) -> int:
    return a + b


print(add_num('a', 'b'))


def menu(entree, drink, dessert):
    print(f'entree: {entree}, drink: {drink}, dessert: {dessert}')


# 位置引数
menu('ice', 'beef', 'beer')  # 順番を間違えたケース
# キーワード引数
menu(dessert='ice', entree='beef', drink='beer')
# 位置引数とキーワード引数の混在
menu('beef', dessert='ice', drink='beer')
# menu(dessert='ice', 'beef', drink='beer')  # Error


def default_menu(entree='beef', drink='wine', dessert='ice'):
    print(f'entree: {entree}, drink: {drink}, dessert: {dessert}')


# デフォルト引数
default_menu()
# 位置引数とキーワード引数とデフォルト引数の混在
default_menu('chicken', drink='beer')


def test_func(x, l=[]):
    l.append(x)
    return l


x1 = [1, 2, 3]
r = test_func(100, x1)
print(r)  # [1, 2, 3, 100]
x2 = [1, 2, 3]
r = test_func(200, x2)
print(r)  # [1, 2, 3, 200]


# 注意
r = test_func(100)
print(r)  # [100]

x3 = [1, 2, 3]
r = test_func(300, x3)
print(r)  # [1, 2, 3, 300]

# 2回目のデフォルト引数の使用時: 前回作成したl=[]のアドレスを指したまま -> l=[]が新たに作成されない
r = test_func(200)
print(r)  # [100, 200]


"""
Pythonでは、call by referenceのもの（list, dict, set）を
デフォルト引数に使うべきではない <- バグの原因
=> Noneを使うと良い！
"""


def sample_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = sample_func(100)
print(r)  # [100]
r = sample_func(200)
print(r)  # [200]


# 複数の引数をタプルにまとめる
def say_something(message, *args):
    print('message: ', message)
    print(args)  # ('Mike', 'Nance')
    for arg in args:
        print(arg)


say_something('Hi!', 'Mike', 'Nance')
t = ('Mike', 'Nance')
say_something('Hi!', *t)  # tuple unpacking


# keyword引数を辞書にまとめる
def menu(**kwargs):
    print(kwargs)  # {'entree': 'beef', 'drink': 'wine', 'dessert': 'ice'}
    for k, v in kwargs.items():
        print(k, v)


menu(entree='beef', drink='wine', dessert='ice')
d = {'entree': 'beef', 'drink': 'wine', 'dessert': 'ice'}
menu(**d)  # dictionary unpacking


# 位置引数、タプル化、辞書化を組み合わせる
# argsはkwargsよりも必ず前に書く（Err）
def menu(food, *args, **kwargs):
    print(f'food: {food}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


menu('banana', 'apple', 'orange', entree='beef', drink='wine')


def example_func(param1, param2):
    """Docstring example for describing overall explanation of function.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    print(param1)
    print(param2)
    return True


print(example_func.__doc__)
# help(example_func)
