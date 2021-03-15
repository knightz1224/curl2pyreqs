#!/bin/env python3
import sys
import getopt
from .ulti import *


def main(**kwags):
    _opts = ['file', 'copy']
    _s_opts = 'FC'
    opt, arg = getopt.getopt(sys.argv[1:], _s_opts, _opts)
    print(convert_main(opt, arg))
