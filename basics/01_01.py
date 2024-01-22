import math


# データの型 -> 変数の型
num = 1
print(num, type(num))
name = 'Mike'
print(name, type(name))
is_ok = True
print(is_ok, type(is_ok))


# 型変換
num = '1'
print(num, type(num))
num = int(num)
print(num, type(num))


# 型宣言（あまり意味ない）
num: int = 1
name: str = 'Mike'
num = name  # エラーにならない！
print(num, type(num))


print('Hi', 'Mike', sep=',')
print('Hi', 'Mike', sep=',', end='!\n')


print(1, type(1))
print(0.6, type(0.6))  # float
17 / 3  # 5.666666666666667
17 // 3  # 5
17 % 3
2**10
pie = 3.14159265358979323846
round(pie, 2)  # 3.14


result = math.sqrt(25)
print(result)  # 5.0
y = math.log2(16)
print(y)  # 4.0
print(help(math))  # ドキュメントを表示
