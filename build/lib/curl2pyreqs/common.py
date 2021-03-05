#!/bin/env python3
import sys
import getopt
from .ulti import *


def main(**kwags):
    _opts = [
        'file',
    ]
    _s_opts = 'F'
    opt, arg = getopt.getopt(sys.argv[1:], _s_opts, _opts)
    if ('-F' in opt[0]) and arg:
        filepath = arg[0]
        parseCurlFile(filepath=filepath)
    else:
        print('Usage:\n\tcurl2pyreqs -F requests.curl')
