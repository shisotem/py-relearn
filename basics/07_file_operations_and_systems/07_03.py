"""
test_dir --(圧縮)--> test.tar.gz --(解凍)--> decompressed_tar
"""
import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')  # 圧縮の対象とするディレクトリを指定

# $ tar -zxvf test.tar.gz -C /tmp  # 解凍して /tmp に展開
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall('decompressed_tar')  # decompressed_tarディレクトリの配下に展開

# 展開せずにファイルの中身を確認
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('test_dir/foo.txt') as f:
        print(f.read())  # b"I'm Foo!\n"
        f.seek(0)  # ファイルの先頭に戻す
        print(f.read().decode('utf-8'))  # I'm Foo!


"""
test_dir --(圧縮)--> test.zip --(解凍)--> decompressed_zip
"""
import zipfile
import glob

# with zipfile.ZipFile('test.zip', 'w') as z:
#     # ディレクトリ名のみならず、その中身まで指定する必要がある
#     z.write('test_dir')
#     z.write('test_dir/test_dir3')
#     z.write('test_dir/foo.txt')
#     z.write('test_dir/bar.txt')

# refactored version
with zipfile.ZipFile('test.zip', 'w') as z:
    # test_dirディレクトリの内部を再帰的に探索
    for f in glob.glob('test_dir/**', recursive=True):
        print(f)
        z.write(f)

# $ unzip test.zip -d /tmp  # 解凍して /tmp に展開
with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('decompressed_zip')

# 展開せずにファイルの中身を確認
with zipfile.ZipFile('test.zip', 'r') as z:
    with z.open('test_dir/foo.txt') as f:
        print(f.read())  # b"I'm Foo!\n"
        f.seek(0)  # ファイルの先頭に戻す
        print(f.read().decode('utf-8'))  # I'm Foo!


# tarファイルもzipファイルも、内部的にはバイナリ形式でデータを格納します。
# これにより、テキストファイル、画像ファイル、動画ファイルなど、あらゆる種類のファイルを
# 一つのアーカイブファイル内に格納することができます。
#
# ファイルを解凍するとき、tarfileやzipfileモジュールはファイルの内容をバイナリ形式のまま返します。
# これにより、プログラムはそのバイナリデータを適切な形式（テキスト、画像、動画など）にデコードすることができます。
#
# たとえば、テキストファイルの場合、バイナリデータは
# 適切な文字エンコーディング（UTF-8、ISO-8859-1など）を使用して文字列にデコードされます。
# 画像ファイルや動画ファイルの場合、バイナリデータは
# 適切な画像や動画のフォーマット（JPEG、PNG、MP4など）にデコードされます。
