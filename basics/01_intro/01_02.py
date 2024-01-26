print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")


print('hello. \nHow are you?')
print(r'C:\name\name')  # r: raw string


print("###############")
print(
    """
line1
line2
line3
"""
)
print("###############")
print("###############")
print(
    """line1
line2
line3"""
)
print("###############")
print("###############")
print(  # 行末の\: 次の行に続くの意
    """\
line1
line2
line3\
"""
)
print("###############")


print("Hi." * 3 + "Mike.")
print("Py" + "thon")
print("Py" "thon")
s = 'aaaaaaaa' 'bbbbbbbb'
print(s)


prefix = "Py"
print(prefix + "thon")  # 変数と文字列の連結には+が必要


word = 'python'
print(word[0])
print(word[-1])
# print(word[100])  # IndexError: string index out of range


print(word[0:2])
print(word[2:6])
print(word[:2])
print(word[2:])
print(word[:2] + word[2:])
print(word[:])


# Pythonの文字列はイミュータブル
word = 'python'
# word[0] = 'j'  # TypeError: 'str' object does not support item assignment
word = 'c' + word[1:]
print(word)


word = 'Rustacean'
n = len(word)
print(n)


s = 'My name is Mike. Hi Mike.'
is_start = s.startswith('My')
print(is_start)
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Bob'))


print('a is {}'.format('test'))
print('a is {} {} {}'.format(1, 2, 3))
print('a is {0} {1} {2}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))
print('My name is {0} {1}. Watashi no namae ha {1} {0}.'.format('Ryo', 'Yamada'))
print(
    'My name is {name} {family}. Watashi no namae ha {family} {name}.'.format(
        name='Ryo', family='Yamada'
    )
)


# f-strings
a = 'test'
print(f'a is {a}')
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
name = 'Ryo'
family = 'Yamada'
print(f'My name is {name} {family}. Watashi no namae ha {family} {name}.')


print(type(str(1)))  # int -> str
print(type(str(3.14)))  # float -> str
print(type(str(True)))  # bool -> str
