__version__ = '0.1.0'

import codecs
import os


def get_ranked():
    lst = []
    path = os.path.dirname(os.path.abspath(__file__))

    for line in codecs.open(path + '/dutch10000-utf8.txt', mode='r', encoding='UTF-8'):
        if line.strip():
            lst.append(line.strip())
    return lst
