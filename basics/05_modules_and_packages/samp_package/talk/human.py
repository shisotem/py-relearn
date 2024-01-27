# from ..tools import utils  # 相対パス: あまり推奨されない
from samp_package.tools import utils  # 絶対パス


def sing():
    return 'sing'


def cry():
    return utils.say_twice('cry')
