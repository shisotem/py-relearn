# print('config:', __name__)


# import configとされただけで処理が実行されてしまうことを防ぐため
if __name__ == '__main__':
    print('config:', __name__)

# __name__が__main__であれば、このスクリプトが直接実行されるということ
# -> config: __main__ と表示されて（処理が実行されて）間違いない

# __name__が__main__でなければ、これはimportされたスクリプトだということ
# -> 処理が実行されてはならない
