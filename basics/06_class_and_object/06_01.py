# intやstrも実はクラス e.g. class str(Sequence[str]):
# objectクラス: 全てのクラスの基底クラス
"""
Pythonでは全てのデータはオブジェクトであり、全てのデータ型（int, str, list, dictなど）は
objectクラスを暗黙的に継承しています。
例えば、int型の値10はintクラスのインスタンスであり、intクラスはobjectクラスを継承しています。
そのため、10は間接的にobjectクラスを継承していると言えます。
"""
print(isinstance(10, int))  # True
print(isinstance(10, object))  # True


# class Person:  # OK(objectクラスを暗黙的に継承している)
# class Person():  # OK(objectクラスを暗黙的に継承している)
class Person(object):  # OK(objectクラスの継承を明示 / Legacy)
    def say_something(self):
        print('hello')


person = Person()
person.say_something()


class Person(object):
    def __init__(self):
        print('init')


person = Person()


class Person(object):
    def __init__(self, name='someone'):
        # インスタンス変数: インスタンスごとに持つ変数
        self.name = name

    def self_introduce(self):
        # インスタンスメソッドの呼び出し
        self.greet()  # <- person.greet()
        print(f'I am {self.name}.')  # <- person.name

    def greet(self, subject='everyone'):
        print(f'Hello, {subject}!')


person = Person('Mike')
person.self_introduce()
print(person.name)


class Person(object):
    def __init__(self, name='someone'):
        self.name = name

    def __del__(self):
        print('good bye')


person = Person('Mike')
del person  # もしくはスクリプトの最後で自動的に削除される


class Car(object):
    def run(self):
        print('run')


class AdvancedCar(Car):
    def auto_run(self):
        print('auto run')


class MyCar(Car):
    def run(self):  # override
        print('my car run')


advanced_car = AdvancedCar()
advanced_car.run()  # run
advanced_car.auto_run()  # auto run

my_car = MyCar()
my_car.run()  # my car run


class Car(object):
    def __init__(self, model=None):
        self.model = model


class MyCar(Car):
    pass


class AdvancedCar(Car):
    def __init__(self, model='sports', enable_auto_run=False):  # override
        # self.model = model
        # super(): 親クラスのメソッドを呼び出す
        # super()が参照するメソッドには自動でインスタンスが渡される -> selfは不要
        super().__init__(model)
        self.enable_auto_run = enable_auto_run


my_car = MyCar('sedan')
print(my_car.model)  # sedan
advanced_car = AdvancedCar('hiace', True)
print(advanced_car.model, advanced_car.enable_auto_run)  # hiace True
