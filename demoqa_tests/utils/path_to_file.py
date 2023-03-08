import os


def define_path(relative_path):
    abs_path = os.path.abspath(
        os.path.join(os.path.dirname(os.curdir), relative_path))
    return abs_path
