from distutils.core import setup


setup(
    name='05_01',
    version='1.0.0',
    packages=['samp_package', 'samp_package.talk', 'samp_package.tools'],
    url='',
    license='',
    author='foo',
    author_email='',
    description='sample package',
)


# $ python setup.py sdist
# source distribution（ソースコード形式での配布）の意味
# dist/tar.gzが作成される
# tar.gz -> エンドユーザに配布 / PyPIにアップロード
