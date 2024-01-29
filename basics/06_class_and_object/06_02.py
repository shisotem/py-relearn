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
# print(advanced_car._enable_auto_run)  # 前述の_varではこの手のアクセスを防げなかったが、
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


"""
ダックタイピング
"""
"""
ダックタイピングとは、オブジェクト指向プログラミングにおける概念で、
Pythonなどの動的型付け言語でよく用いられます。この概念は、
「もし何かがアヒルのように歩き、アヒルのように鳴くなら、それはアヒルであろう」
というフレーズから名付けられました。
具体的には、オブジェクトの型やクラスをチェックするのではなく、
そのオブジェクトが期待するメソッドや属性を持っているかどうかをチェックします。
つまり、オブジェクトの振る舞いが重要であり、
そのオブジェクトが何であるか（どのクラスからインスタンス化されたか）は重要ではありません。
"""


class Car(object):
    def ride(self, person):
        person.drive()


class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('OK')
        else:
            raise Exception('No drive')


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError


baby = Baby()
car = Car()
# car.ride(baby)  # Exception: No drive

adult = Adult()
car = Car()
car.ride(adult)  # OK

# このようにダックタイピングでは、メソッドの振る舞いを中心に記述していく


"""
抽象クラス(インスタンス化できない・継承されて使うことを前提としたクラス)
"""
# Pythonでは抽象クラスを使わなくても同じような実装が可能なため、
# 特に必要がなければJavaの思想を入れずにPythonicに書くべき(つまりあまり使わないべき)

import abc


class Person(metaclass=abc.ABCMeta):  # 抽象クラス
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod  # 抽象メソッド
    def drive(self):  # driveメソッドの実装を子クラスに強制する(-> 実装忘れを防ぐ)
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):  # 実装を忘れるとエラー
        raise Exception('No drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):  # 実装を忘れるとエラー
        print('OK')


baby = Baby()
# baby.drive()  # Exception: No drive

adult = Adult()
adult.drive()  # OK


"""
多重継承
"""


class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')


class Car(object):
    def run(self):
        print('car run')


class PersonCarRobot(Person, Car):  # 多重継承(左から優先度が高い)
    def fly(self):
        print('fly')


person_car_robot = PersonCarRobot()
person_car_robot.talk()  # talk
person_car_robot.run()  # person run
person_car_robot.fly()  # fly

# (可能であれば)多重継承を使わない設計にした方が良い
# 多重継承を使わなければならないケースもあるが、継承の順番による予期せぬバグに注意する


"""
クラス変数 -> オブジェクト間で値を共有できる
"""


class Person(object):
    kind = 'human'  # クラス変数

    def __init__(self, name):
        self.name = name  # インスタンス変数

    def who_are_you(self):
        print(self.name, self.kind)  # クラス変数も self.kind のように参照する


t = Person('Taro')
t.who_are_you()  # Taro human
b = Person('Bob')
b.who_are_you()  # Bob human


class T(object):
    words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word('add 1')
c.add_word('add 2')

d = T()
d.add_word('add 3')
d.add_word('add 4')

print(c.words)  # ['add 1', 'add 2', 'add 3', 'add 4']


"""
クラスメソッド: クラス変数にアクセスする必要がある場合(或いはクラス自体の操作)
"""


class Person(object):
    kind = 'human'  # クラス変数

    def __init__(self):
        self.x = 100  # インスタンス変数

    def what_is_your_kind(self):  # インスタンスメソッド
        return self.kind  # 内からは、self.kind でクラス変数を参照

    @classmethod
    def tell_me_your_kind(cls):  # クラスメソッド
        return cls.kind  # 内からは、cls.kind でクラス変数を参照


# self: インスタンス自体を参照するための変数
# cls: クラス自体を参照するための変数


a = Person()  # オブジェクトを生成
print(a)  # <__main__.Person object at 0x102664390>
print(a.x)  # 100
print(a.what_is_your_kind())  # human
print(a.kind)  # human(クラス変数はインスタンスからも参照できる)
print(a.tell_me_your_kind())  # human(クラスメソッドはインスタンスからも参照できる)

b = Person  # クラスそのもの
print(b)  # <class '__main__.Person'>
# print(b.x)  # AttributeError(インスタンス変数はクラスからは参照できない)
# print(b.what_is_your_kind())  # missing 1 required positional argument: 'self'
print(b.kind)  # human(クラス変数はクラスからも参照できる)
print(b.tell_me_your_kind())  # human(クラスメソッドはクラスからも参照できる)

print(Person.kind)  # human(クラス変数はクラスからも参照できる)
print(Person.tell_me_your_kind())  # human(クラスメソッドはクラスからも参照できる)

"""
<まとめ: アクセスOK/NG>

- インスタンス
    * インスタンス変数: OK
    * インスタンスメソッド: OK
    * クラス変数: OK
    * クラスメソッド: OK
  
- クラス
    * インスタンス変数: NG!
    * インスタンスメソッド: NG!
    * クラス変数: OK
    * クラスメソッド: OK
"""


"""
スタティックメソッド: (クラスと論理的に関連しているが)クラス変数にアクセスする必要がない場合
"""


class Person(object):
    @staticmethod
    def about():  # スタティックメソッド
        print('about human')


Person.about()  # about human (関数名の競合を避ける)名前空間としての役割も果たす


class Person(object):
    @staticmethod
    def about(year):
        print('about human {}'.format(year))


Person.about(1999)  # about human 1999


# スタティックメソッドは、クラスとの関連性が薄く、"クラスのデータにアクセスしない"ため、
# クラスの外側に関数として作成しても機能的に問題がない
def about(year):
    print('about human {}'.format(year))


class Person(object):
    pass


about(1999)  # about human 1999
# しかし、クラスに関連する処理であることを示したい場合には、
# スタティックメソッドを使用する意味はあるということである


"""
特殊メソッド(Magic Methods)
"""


# __str__(): print()やstr()実行時に内部的に呼び出される
class Word(object):
    def __init__(self, text):
        self.text = text

    # objectクラスの__str__()をoverrideした
    def __str__(self):
        return 'This is Word object (text={})'.format(self.text)


w = Word('test')
# override前は元々、<__main__.Word object at 0x100624b50> という出力だったが、
print(w)  # This is Word object (text=test)
s = str(w)
print(s)  # This is Word object (text=test)


# __len__(): len()実行時に内部的に呼び出される
class Word(object):
    def __init__(self, text):
        self.text = text

    # 新たに定義（objectクラスには__len__()は定義されていないためoverrideではない）
    def __len__(self):
        return len(self.text)  # 注: いつものlen(str)


w = Word('test')
# __len__()定義前は元々、TypeError: object of type 'Word' has no len() という出力だったが、
print(len(w))  # 4 (ユーザ定義のlen(Word))


# __add__(): Wordクラスのオブジェクト同士が +演算された時に内部的に呼び出される
class Word(object):
    def __init__(self, text):
        self.text = text

    # 新たに定義（objectクラスには__add__()は定義されていないためoverrideではない）
    def __add__(self, word):  # w2が引数wordに渡される
        return self.text.capitalize() + word.text.capitalize()  # 注: 通常のstr+str


w = Word('hello')
w2 = Word('world')
# __add__()定義前は元々、TypeError: unsupported operand type(s) for +: 'Word' and 'Word' という出力だったが、
print(w + w2)  # HelloWorld (ユーザ定義のWord+Word)


# __eq__(): Wordクラスのオブジェクト同士が ==演算された時に内部的に呼び出される
class Word(object):
    def __init__(self, text):
        self.text = text

    # objectクラスの__eq__()をoverrideした
    def __eq__(self, word):  # w2が引数wordに渡される
        return self.text == word.text  # 注: 通常のstr==str


w = Word('test')
w2 = Word('test')
# override前は元々、w==w2: False, id(w): 4330347280, id(w2): 4330349072 という出力だったが（オブジェクトの非同一性）、
print(
    f'w==w2: {w==w2}, id(w): {id(w)}, id(w2): {id(w2)}'
)  # w==w2: True, id(w): 4330347280, id(w2): 4330349072
