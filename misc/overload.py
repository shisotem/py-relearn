from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')


@add.register(int)
def _(a, b):
    print(f'First arg is of type {type(a)}: {a + b}')


@add.register(str)
def _(a, b):
    print(f'First arg is of type {type(a)}: {a + b}')


# (2) First arg is of type <class 'int'>: 3
add(1, 2)
# (3) First arg is of type <class 'str'>: aB
add('a', 'B')
# (2) TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
add(1, None)
# (1) NotImplementedError: Unsupported type
add(None, 1)
