"""
カプセル化（プロパティ・プライベート変数）
"""


class Car(object):
    def __init__(self, model=None):
        self.model = model


class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run


advanced_car = AdvancedCar('SUV')
print(advanced_car.enable_auto_run)  # False
advanced_car.enable_auto_run = True  # インスタンス変数はクラス外から変更できてしまう
print(advanced_car.enable_auto_run)  # True


# このように書き換えられたく無い場合、
# プロパティ（getter/setter/deleterからなるカプセル化のための機能）を使う
# getter: @property
# setter: @<property_name>.setter
# deleter: @<property_name>.deleter
class Car(object):
    def __init__(self, model=None):
        self.model = model


class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        # _var(__var): プライベート変数（クラス外部から直接アクセスされるべきではないことを表す）
        self._enable_auto_run = enable_auto_run

    # @propertyにより、()なしで変数のように呼び出せる（メソッドを属性のように扱える）
    @property
    def enable_auto_run(self):  # getter
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):  # setter
        self._enable_auto_run = is_enable


# getter only時
advanced_car = AdvancedCar('SUV')
print(advanced_car.enable_auto_run)  # False
# advanced_car.enable_auto_run = True  # AttributeError

# getter + setter時
advanced_car.enable_auto_run = True  # is_enableにTrueが渡される
print(advanced_car.enable_auto_run)  # True


# 普通の変数ではなく、getter/setterを使うメリット
# ->「特定の条件に合致した時のみ書き換え可能」にすることができる
# e.g. passwdがasdfの時のみ書き換え可能
class Car(object):
    def __init__(self, model=None):
        self.model = model


class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False, passwd=''):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == 'asdf':  # passwdをasdfに設定しておく
            self._enable_auto_run = is_enable
        else:
            raise ValueError('passwd is wrong')


advanced_car = AdvancedCar('SUV', passwd='asdf')  # passwd: asdfでトライ
print(advanced_car.enable_auto_run)  # False
advanced_car.enable_auto_run = True  # 変更成功
print(advanced_car.enable_auto_run)  # True

advanced_car = AdvancedCar('SUV', passwd='foo')  # passwd: fooでトライ
print(advanced_car.enable_auto_run)  # False
# advanced_car.enable_auto_run = True  # ValueError: passwd is wrong


# __var: name manglingというプロセスを経て、内部的に_ClassName__varという名前に変換される
# -> クラス外からの直接アクセスが_varより困難だが、manglingされた名前を知っていればアクセス可能ではある
# (note: 子クラスと親クラスの両方で同名の__varを定義すると、manglingを経て、
# それぞれ別の変数として扱われるため、子クラスが親クラスの変数を意図せず上書きしてしまうことを防げる)
class Car(object):
    def __init__(self, model=None):
        self.model = model


class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    def check(self):
        print(self.__enable_auto_run)  # クラス内部からは__varにアクセス可能


advanced_car = AdvancedCar('SUV')
# print(advanced_car._enable_auto_run)  # 前述の_varではこのアクセスを防げない
# print(advanced_car.__enable_auto_run)  # __varはこれを防げる(AttributeError)

print(advanced_car.enable_auto_run)  # getterによる正しいアクセス方法(False)
print(advanced_car._AdvancedCar__enable_auto_run)  # ずるいアクセス(False)

advanced_car.check()  # False


# [注意]
# クラス外部からの変数の追加は一般に可能
class T(object):
    pass


t = T()
t.age = 20
t.name = 'Taro'
print(t.age, t.name)  # 20 Taro


# __varのクラス外部からの書き換えを試みると、これが起きる
class Car(object):
    def __init__(self, model=None):
        self.model = model


class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run


advanced_car = AdvancedCar('SUV')
advanced_car.__enable_auto_run = 'Foo'

print(advanced_car._AdvancedCar__enable_auto_run)  # False
print(advanced_car.__enable_auto_run)  # Foo(新しい変数が追加されてしまった)

