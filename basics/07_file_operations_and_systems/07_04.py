"""
一時ファイル
"""
import tempfile

# メモリ(I/Oバッファ)上に、一時ファイルを作成 -> プログラム終了時に自動削除
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())  # hello

# ディスク上に、実際に一時ファイルを作成 -> t.nameという名前で保存される -> 削除する必要あり
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)  # /var/folders/0j/lsxbrtnx18d4rvgrp55czc700000gn/T/tmpdij78pkf
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())  # test

# $ bat --show-all /var/folders/0j/lsxbrtnx18d4rvgrp55czc700000gn/T/tmpdij78pkf
# test␊

import os

os.remove(t.name)

"""
一時ディレクトリ -> 中でファイルを作成し圧縮するなどといった活用も可能
"""
with tempfile.TemporaryDirectory() as td:
    print(td)  # /var/folders/0j/lsxbrtnx18d4rvgrp55czc700000gn/T/tmpcmxvsaef -> 自動削除

temp_dir = tempfile.mkdtemp()
print(
    temp_dir
)  # /var/folders/0j/lsxbrtnx18d4rvgrp55czc700000gn/T/tmpv5f2x7m3 -> 削除する必要あり

os.rmdir(temp_dir)


"""
subprocess
"""
import subprocess

subprocess.run(['ls', '-a'])  # . .. .git .gitignore README.md applications basics

# Legacyで非推奨 (-> subprocessを使う)
# os.system('ls -a')  # . .. .git .gitignore README.md applications basics

# 文字列でコマンドを実行可能
# 注: シェルインジェクションの危険性 e.g. $ rm -rf /
subprocess.run('ls -a | grep *.md', shell=True)  # README.md


r = subprocess.run('hoge', shell=True)  # /bin/sh: hoge: command not found
print(f'r.returncode: {r.returncode} (このように0以外の場合は異常終了)')
print('shell=True -> 異常終了でも処理が止まらず、引き続き実行されてしまう!')


"""
datetime・バックアップファイル
"""
