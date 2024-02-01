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
# os.system() は、Legacyで非推奨 (-> subprocessを使う)
# os.system('ls -a')  # . .. .git .gitignore README.md applications basics

import subprocess

# リスト形式でコマンドを実行
subprocess.run(['ls', '-a'])  # . .. .git .gitignore README.md applications basics

# # ちゃんと実行中断される!
# subprocess.run(['hoge'])  # FileNotFoundError: [Errno 2] No such file or directory: 'hoge'


# 文字列形式でコマンドを実行(shell=True)
# 注: シェルインジェクションの危険性あり e.g. $ rm -rf /
subprocess.run('ls -a | grep .*\.md$', shell=True)  # README.md

r = subprocess.run('hoge', shell=True)  # /bin/sh: hoge: command not found
print(f'r.returncode: {r.returncode} (このようにリターンコードが0以外の場合は異常終了)')
print('shell=True の場合、異常終了なのに処理が止まらず、引き続き実行されてしまう!')

# # なので、Exceptionをraiseするような処理を自分で書いたり、
# if r.returncode != 0:
#     raise Exception(f"'hoge' command failed with return code {r.returncode}")

# # あるいは、check=Trueを指定する
# subprocess.run(
#     'hoge', shell=True, check=True
# )  # subprocess.CalledProcessError: Command 'hoge' returned non-zero exit status 127.


# Popenを使えば、リスト形式でもパイプライン処理は可能
p1 = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', '.*\.md$'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)  # b'README.md\n'


"""
datetime・time (バックアップファイルの作成)
"""
import datetime

now = datetime.datetime.now()
print(now)  # 2024-02-02 00:36:28.572636
print(now.isoformat())  # 2024-02-02T00:36:28.572636
print(
    now.strftime('%Y / %m / %d ( %H : %M : %S . %f )')
)  # 2024 / 02 / 02 ( 00 : 36 : 28 . 572636 )

today = datetime.date.today()
print(today)  # 2024-02-02
print(today.isoformat())  # 2024-02-02
print(today.strftime('%Y / %m / %d'))  # 2024 / 02 / 02

# 任意の時刻を作成
t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)  # 01:10:05.000100
print(t.isoformat())  # 01:10:05.000100
print(t.strftime('%H / %M / %S . %f'))  # 01 / 10 / 05 . 000100

# 時刻の計算
now = datetime.datetime.now()
print(now)  # 2024-02-02 00:36:28.572636

delta_neg = datetime.timedelta(weeks=-1)
print(now + delta_neg)  # 2024-01-26 00:36:28.572636
delta_pos = datetime.timedelta(weeks=1)
print(now - delta_pos)  # 2024-01-26 00:36:28.572636

d = datetime.timedelta(days=365)
print(now + d)  # 2025-02-01 00:36:28.572636


import time

print('## start')
time.sleep(2)
print('## end')

# UNIX時間(エポックタイム): 1970/01/01 00:00:00 (= epoch) からの経過秒数
print(time.time())  # 1706803028.724313


# バックアップファイルの作成
import shutil

now = datetime.datetime.now()
file_name = 'backup_test.txt'

# バックアップを取っておく
if os.path.exists(file_name):
    shutil.copy(file_name, f'{file_name}.{now.strftime("%Y_%m_%d_%H_%M_%S")}')

# オリジナルに変更を加える
with open(file_name, 'a') as f:
    f.write('This is a backup test file.\n')
