import sys, os

_BASEDIR_ = os.path.dirname(__file__)
sys.path.append(_BASEDIR_)

from src.connection import Connection



if __name__ == '__main__':
    conn = Connection()
    conn.send("data")
