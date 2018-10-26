import os
from preprint import pre_print, over_print
from main import _main as call_main

basedir=os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    pre_print()
    call_main(basedir)
    over_print()
