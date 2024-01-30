import string

s = """\
Hi $name.
$contests
Have a nice day.
"""

t = string.Template(s)  # t: Templateオブジェクト
contests = t.substitute(name='Mike', contests='How are you?')
print(contests)
# Hi Mike.
# How are you?
# Have a nice day.

"""
Pythonでは、if文、for文、with文などのブロック内で宣言された変数は、
そのブロックの外からもアクセス可能です。
これは、これらのブロックが"新しいスコープを作成しない"ためです。

関数やクラスの定義内で宣言された変数は、
その関数やクラスの内部からのみアクセス可能で、これらはローカル変数と呼ばれます。
これは、関数とクラスが"新しいスコープを作成する(*)"ためです。
(*): 関数、クラス（、内包表記、モジュール）のみ

ただし、globalキーワードを使用して関数内で変数を宣言すると、
その変数はグローバルスコープになります。
同様に、nonlocalキーワードを使用すると、
エンクロージングスコープ（囲んでいるスコープ）の変数にアクセスできます。
"""
# open: デフォルトで'r'モード
with open('design/email_template.txt') as f:
    t = string.Template(f.read())

contests = t.substitute(name='Mike', contests='How are you?')
print(contests)
# -> このようにテンプレートファイルを読み込み専用で扱えば、オリジナルを汚染する心配がない


# Tips: (MacOS) $ open test.csv
import csv

with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()  # ヘッダーを書き込む (ファイルが作成される)

    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])
# A 1
# B 2


import os

print(os.path.exists('test.csv'))  # True (パス(file/dir)が存在するか)
print(os.path.isfile('test.csv'))  # True (ファイルかどうか)
print(os.path.isdir('design'))  # True (ディレクトリかどうか)

# os.rename('test.txt', 'renamed.txt')
# os.symlink('renamed.txt', 'symlink.txt')  # シンボリックリンクの作成

# os.mkdir('test_dir')
# os.rmdir('test_dir')

import pathlib

pathlib.Path('empty.txt').touch()  # 空のファイルを作成
os.remove('empty.txt')  # ファイルを削除


# os.mkdir('test_dir')  # 準備
# os.mkdir('test_dir/test_dir2')  # 準備
# os.mkdir('test_dir/test_dir3')  # 準備
# pathlib.Path('test_dir/foo.txt').touch()  # 準備
# pathlib.Path('test_dir/bar.txt').touch()  # 準備

# ディレクトリの内容をリストアップ
print(os.listdir('test_dir'))  # ['foo.txt', 'bar.txt', 'test_dir2', 'test_dir3']

import glob

# 特定のパターンに一致するファイルを検索(listdirよりも柔軟)
print(
    glob.glob('test_dir/*')
)  # ['test_dir/foo.txt', 'test_dir/bar.txt', 'test_dir/test_dir2', 'test_dir/test_dir3']


import shutil

shutil.copy('test_dir/foo.txt', 'test_dir/test_dir2/baz.txt')  # ファイルをコピー
# print(glob.glob('test_dir/test_dir2/*'))  # ['test_dir/test_dir2/baz.txt']

# shutil.rmtree('test_dir/test_dir2')  # $ rm -rf test_dir2
