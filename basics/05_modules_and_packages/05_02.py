"""
built-in functions (imported by default)
"""
print(globals())
# {...
# '__builtins__': <module 'builtins' (built-in)>,
# ...}
# 'builtins': 組み込み関数のライブラリ
__builtins__.print('Hello, World!')

ranking = {'A': 100, 'B': 85, 'C': 95}
print(ranking.get('A'))  # 100
print(ranking.get)  # <built-in method get of dict object at 0x1023f9f00>
sorted(ranking, key=ranking.get, reverse=True)  # ['A', 'C', 'B']


"""
stdlib
"""
s = 'awdswdasswdaaaddwwwaasdawdaaawwasdwwwdads'
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)  # {'a': 13, 'w': 12, 'd': 10, 's': 6}

d = {}
for c in s:
    d.setdefault(c, 0)  # キーcに対応するvalueが無い場合、d[c] = 0で初期化
    d[c] += 1
print(d)

from collections import defaultdict

# 初期値が0となるdefaultdict型オブジェクトを生成
d = defaultdict(int)  # int()は0を返す関数
print(type(d))  # <class 'collections.defaultdict'>
for c in s:
    d[c] += 1
print(d)  # defaultdict(<class 'int'>, {'a': 13, 'w': 12, 'd': 10, 's': 6})


"""
3rd-party libraries
"""
from termcolor import colored

print(colored('Hello, World!', 'red'))
# help(colored)  # colored関数のヘルプ


# import collections, sys, os  # 非推奨
"""
import collections  # stdlibをアルファベット順に並べる
import os
import sys

import termcolor  # 1行空けて3rd-partyのセクション

import samp_package  # 1行空けて同プロジェクトの他チームのパッケージのセクション

import config  # 1行空けて自作ライブラリのセクション
"""

# * VSCode: Go To Definition
# - stdlib
# e.g. python3.11/collections/__init__.py
# e.g. python3.11/uuid.py
# - 3rd-party
# e.g. python3.11/site-packages/termcolor/__init__.py

import collections

import termcolor

import samp_package

import config

print(collections.__file__)
print(termcolor.__file__)
print(samp_package.__file__)
print(config.__file__)
# /Users/.../python3.11/collections/__init__.py
# /Users/.../python3.11/site-packages/termcolor/__init__.py
# /Users/.../py-relearn/.../05_modules_and_packages/samp_package/__init__.py
# /Users/.../py-relearn/.../05_modules_and_packages/config.py


# Pythonがパッケージを読み込む際に参照するPATH
import sys

print(sys.path)
# 優先順位: カレントディレクトリ > stdlib > 3rd-party
"""
[
    '/Users/.../py-relearn/basics/05_modules_and_packages',  # カレントディレクトリ
    '/Users/.../.asdf/installs/python/3.11.7/lib/python311.zip', 
    '/Users/.../.asdf/installs/python/3.11.7/lib/python3.11',  # stdlib
    '/Users/.../.asdf/installs/python/3.11.7/lib/python3.11/lib-dynload', 
    '/Users/.../.asdf/installs/python/3.11.7/lib/python3.11/site-packages'  # 3rd-party
]
"""


"""
__name__について
"""
# このスクリプトがPython側で実行しているメインのスクリプトだということ
print('05_02:', __name__)  # 05_02: __main__

# config.pyの中に実行できる処理がある場合、importしただけで実行されてしまう
import config  # config: config (<-ファイル名)


# この05_02.pyも、このようにmain関数に処理を纏めるとよい
"""
def main():
    # ここに処理を書く
    ...
    
if __name__ == '__main__':
    main()
"""
