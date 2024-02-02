import os


def is_data_present(filename):
    try:
        if os.stat(filename).st_size > 0:
            return True
        else:
            return False
    except FileNotFoundError:
        return False
