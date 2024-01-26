# 例外処理（error handling）: err発生時に実行する処理のこと
l = [1, 2, 3]
i = 5
try:
    l[i]
except:
    print("Don't worry")
print("End")

l = [1, 2, 3]
i = 5
try:
    l[i]
except IndexError as ex:
    print(f"Don't worry: {ex}")
print("End")

l = [1, 2, 3]
i = 5
del l
try:
    l[i]
except IndexError:
    print("Don't worry: IndexError")
except NameError:
    print("Don't worry: NameError")
print("End")

# よくわからないがExceptionでとりあえず纏めてキャッチする
# -> Pythonではあまり推奨されない書き方
l = [1, 2, 3]
i = 5
try:
    () + l
except IndexError as ex:
    print(f"Don't worry: {ex}")
except NameError as ex:
    print(f"Don't worry: {ex}")
except Exception as ex:
    print(f"Don't worry: {ex}")
print("End")


l = [1, 2, 3]
i = 5
try:
    l[i]
except IndexError as ex:
    print(f"Don't worry: {ex}")
finally:
    print('finally: Errが発生してもしなくても実行される')
print("End")

# l = [1, 2, 3]
# i = 5
# del l
# try:
#     l[i]
# except IndexError as ex:
#     print(f"Don't worry: {ex}")
# finally:
#     print('finally: Errが処理されずにプログラムが中断しても実行される')
# print("End")


l = [1, 2, 3]
i = 2
try:
    l[i]
except IndexError as ex:
    print(f"Don't worry: {ex}")
else:
    print('else: Errが発生しなかった場合にのみ実行される')
print("End")


# 例外を発生させる
# raise IndexError('test error')


# 独自例外の作成（エラークラスの自作）-> わかりやすいエラーを作って開発効率アップ！


# Exceptionを継承したUppercaseErrorを作成
# 実装がpassのみなので機能はExceptionと同じ
class UppercaseError(Exception):
    pass


def check():
    words = ['apple', 'orange', 'BANANA']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


# check()  # UppercaseError: BANANA

try:
    check()
except UppercaseError as exc:
    print(f'This is my fault. Go next: {exc}')
