a = 2
b = 2
if a > 0 and b > 0:
    print('a and b are positive')
a = 1
b = -1
if a > 0 or b > 0:
    print('a or b is positive')


y = [1, 2, 3]
x = 1
if x in y:
    print('x is in y')
if 100 not in y:
    print('100 is not in y')


# notを==や<に使用することは推奨されない
# if not x == y: -> if x != y:
# if not x < y: -> if x >= y:


# notの良い使用例
is_ok = True
if is_ok:
    print('hello')
is_ok = False
if not is_ok:
    print('goodbye')


# 0や空文字はFalsy
is_ok = 1024
if is_ok:
    print('OK!')
else:
    print('No!')
is_ok = 0
if is_ok:
    print('OK!')
else:
    print('No!')
is_ok = 'macbook'
if is_ok:
    print('OK!')
else:
    print('No!')
is_ok = ''
if is_ok:
    print('OK!')
else:
    print('No!')


"""
以下の値は全てfalsyと評価されます:
- None
- False
- 0、0.0、0j(実部と虚部が0の複素数)
- 空の文字列、リスト、タプル、辞書、セット
これら以外の値は全てtruthyと評価されます。
"""


is_ok = []
if len(is_ok) > 0:
    print('OK!')
else:
    print('No!')
# リストでは特に有用
is_ok = []
if is_ok:
    print('OK!')
else:
    print('No!')


# None（: 値がないことを表す）の判定にはisを使用する
print(None, type(None))  # None <class 'NoneType'>
# print(help(None))


# よくない例
is_empty = None
if is_empty == None:
    print('None!!!')
# よい例
is_empty = None
if is_empty is None:
    print('None!!!')
is_empty = 'foo'
if is_empty is not None:
    print('Foo!!!')


# isはオブジェクト同士が同一か否か（メモリ上の同一性）を判定する
print(1 == True)  # True（1はtruthyな値）
print(1 is True)  # False
print(1 is not True)  # True
print(True is True)  # True
print(None is None)  # True


print(id(1), id(True))  # 4386975440 4385967272
print(id(True), id(True))  # 4385967272 4385967272
print(id(None), id(None))  # 4386050408 4386050408


"""
Pythonのid()関数は、引数として与えられたオブジェクトの一意の識別子を返します。
この識別子は、オブジェクトがメモリ上に存在する間は変わらず、そのオブジェクトの
ライフタイム中は一意であることが保証されています。
具体的には、id()関数はオブジェクトのメモリアドレスを返すことが多いですが、
これはPythonの実装やプラットフォームに依存します。Pythonの公式ドキュメンテーションでは、
id()関数の返す値は「オブジェクトの識別子」とだけ説明されています。
したがって、あなたのコードのid(1)、id(True)、id(None)はそれぞれ、
整数の1、ブール値のTrue、Noneオブジェクトの識別子を表示しています。
"""

"""
PythonではNoneの判定にisを使うのが一般的です。
これはNoneがシングルトン（プログラム全体でただ1つしか存在しないオブジェクト）であるためです。
NoneはPythonで未定義の値を表す特殊な値で、全てのNoneオブジェクトは同一です。
したがって、isを使ってNoneの同一性を確認することが推奨されます。
==演算子は値の等価性をチェックしますが、
is演算子はオブジェクトの同一性（つまり、同じオブジェクトであるか）をチェックします。
Noneの場合、これらは同じ結果を返しますが、isを使うことで意図が明確になります。
また、isを使うことで、オブジェクトがNoneであるかどうかを最も効率的に確認することができます。
"""

"""
PythonにはNone以外にもいくつかのシングルトンが存在します。以下にその例を挙げます：
- True: 真を表すブール値。全てのTrueオブジェクトは同一です。
- False: 偽を表すブール値。全てのFalseオブジェクトは同一です。
- NotImplemented: 演算子の特殊メソッド（__add__や__lt__など）が操作を実装していないことを示す特殊な値。全てのNotImplementedオブジェクトは同一です。
- Ellipsis: ...とも書かれ、主にスライス操作で使われます。全てのEllipsisオブジェクトは同一です。
これらのシングルトンもNoneと同様に、その同一性を確認するためにis演算子を使うことが推奨されます。
"""
