# f = open('test.txt', 'w')  # デフォルトでカレントディレクトリに作成
# f.write('This is a test')
# f.close()

# f = open('test.txt', 'a')  # append
# f.write('!!!')
# f.close()  # メモリが解放される

# # printよりもwriteの方がよく使われる
# f = open('test.txt', 'w')
# print('This', 'is', 'a', 'pen', sep='/', end='!', file=f)
# f.close()

s = """\
AAA
BBB
CCC
"""
# closeし忘れないために、with文を使うのが良いとされている
# インデント内の処理が全て終了した時に自動でf.close()される
with open('test.txt', 'w') as f:
    f.write(s)

with open('test.txt', 'r') as f:
    print(f.read())

# 1行ずつ読み込む
with open('test.txt', 'r') as f:
    while True:
        # もし行が空なら''が返る -> ''はfalsy -> not line(ラインがないなら)
        line = f.readline()
        print(line, end='')  # 改行が2重になるのでprintの改行をなくす
        if not line:
            break

# かたまり(chunk)毎に読み込む  e.g. パケットを読み込むプログラム
with open('test.txt', 'r') as f:
    while True:
        chunk = 2  # 2文字ずつ読み込む(\nも1文字としてカウント)
        line = f.read(chunk)
        print(line)
        if not line:
            break
"""
AA
A

BB
B

CC
C

"""


with open('test.txt', 'r') as f:
    # tell: ファイル内の位置 (カーソルの位置のイメージ)
    print(f.tell())  # 0 (->次は0始まり0番目のidxから読み込む)
    print(f.read(1))  # A
    print(f.tell())  # 1 (->次は0始まり1番目のidxから読み込む)
    print(f.read(3))  # AA\n
    print(f.tell())  # 4 (->次は0始まり4番目のidxから読み込む)

with open('test.txt', 'r') as f:
    f.seek(4)  # 0始まり4番目のidxにカーソルを移動
    print(f.read(3))  # BBB
    f.seek(0)  # 0始まり0番目のidxにカーソルを戻す
    print(f.read(3))  # AAA


# 書き込みと読み込みを同時に行う
with open('test.txt', 'w+') as f:
    # [注: w+で開いた時点でファイルは一度空になる]
    f.write(s)  # 書き込んだ後はカーソルが末尾に移動しているので、
    f.seek(0)  # 0始まり0番目のidxにカーソルを戻す必要がある
    print(f.read())  # AAA\nBBB\nCCC\n

# 読み込みと書き込みを同時に行う
# r+ではファイルが読み込めないとエラー
with open('test.txt', 'r+') as f:
    print(f.read())  # AAA\nBBB\nCCC\n
    f.seek(0)  # 0始まり0番目のidxにカーソルを戻す
    f.write(s)  # 上書き (上書きされなかった部分はそのまま残る)
