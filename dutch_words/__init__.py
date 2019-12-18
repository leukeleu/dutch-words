__version__ = '0.1.0'

import codecs
import os


def get_ranked():
    path = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(path, 'dutch10000-utf8.txt')) as file:
        return file.read().splitlines()
