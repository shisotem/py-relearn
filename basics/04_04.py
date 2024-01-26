"""
スクリプト04_04.py最上部のdocstring
"""
animal = 'cat'  # global variable


def f():
    print(animal)  # 関数内からグローバル変数を参照


# f()  # cat


animal = 'cat'  # global variable


def f():
    print(animal)  # UnboundLocalError(local変数を作成する前に出力しようとしていると見做される)
    animal = 'dog'  # local変数の作成(注: global変数の変更ではない)


# f()


animal = 'cat'  # global variable


def f():
    animal = 'dog'  # local変数の作成(注: global変数の変更ではない)
    print('local:', animal)  # dog


# f()
# print('global:', animal)  # cat


# 関数内からglobal変数を変更する方法
animal = 'cat'  # global variable


def f():
    global animal  # global文: 列挙した識別子をグローバル変数として解釈するよう指定する
    animal = 'dog'  # global変数の変更
    print('local:', animal)  # dog


# f()
# print('global:', animal)  # dog


"""
ローカル変数やグローバル変数の出力について
"""
star = 'deneb'
animal = 'cat'


def foo():
    """foo関数のdocstring"""

    def inner():
        pass  # null operation

    inner()
    star = 'sirius'
    animal = 'dog'

    print('local: ', locals())
    # local:  {
    #     'inner': <function foo.<locals>.inner at 0x104728d60>,
    #     'star': 'sirius', 'animal': 'dog'
    # }

    # dundarはPythonが使用する特殊な変数
    print(foo.__name__)  # foo
    print(foo.__doc__)  # foo関数のdocstring


foo()


print('global: ', globals())
"""
global:  {
    '__name__': '__main__',  # -> Pythonが最初にこのスクリプトを実行したということ！
    '__doc__': '\nスクリプト04_04.py最上部のdocstring\n', 
    
    '__package__': None, 
    '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x100919450>, 
    '__spec__': None, 
    '__annotations__': {}, 
    '__builtins__': <module 'builtins' (built-in)>, 
    '__file__': '/Users/.../py-relearn/basics/04_04.py', 
    '__cached__': None, 
    
    'animal': 'cat', 
    'f': <function f at 0x100940a40>, 
    'star': 'deneb', 
    'foo': <function foo at 0x1008bc4a0>
}
"""
