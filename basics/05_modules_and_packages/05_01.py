"""
import sys

print(sys.argv)  # ['/Users/.../basics/05_01.py', 'option1', 'option2']
for arg in sys.argv[1:]:
    print(arg)
"""


# 普段使いには長すぎるが、どこで作られたパッケージか分かりやすいという利点がある
"""
import samp_package.utils

print(samp_package.utils.say_twice('hoge'))
"""

# こちらの方が普通(モジュール単位でのimport)
"""
from samp_package import utils

print(utils.say_twice('hoge'))
"""

# 関数だけをimportすることもできるが、推奨されない(名前空間が衝突する可能性)
"""
from samp_package.utils import say_twice

print(say_twice('hoge'))
"""

# モジュール名が非合理に長い場合にのみ使用してもよい(濫用すると可読性が下がる)
"""
from samp_package import utils as u

print(u.say_twice('hoge'))
"""


"""
from samp_package.talk import human

print(human.sing())
"""

# 以降samp_package/utils.pyをsamp_package/tools/utils.pyにmv

"""
from samp_package.talk import human

print(human.cry())  # cry!cry!
"""


"""
# *によるimport（非推奨: 何が読み込まれているか曖昧）
# __init.py__内に__all__を定義する必要がある
from samp_package.talk import *

print(animal.sing())
print(animal.cry())
print(human.sing())
print(human.cry())
"""


# ImportErrorへの対処

# try-except: パッケージはバージョンによってファイルパスが異なることがあるが、
# どのバージョンでもエラーとならないようにするために有用な方法
try:
    from samp_package import utils
except ImportError:
    from samp_package.tools import utils

print(utils.say_twice('hoge'))
