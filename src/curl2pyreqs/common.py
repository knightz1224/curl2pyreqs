#!/bin/env python3
import sys
import os
import getopt
from .ulti import *
from rich.console import Console


def main(**kwags):
    _opts = ['file', 'copy']
    _s_opts = 'FC'
    opt, arg = getopt.getopt(sys.argv[1:], _s_opts, _opts)
    color, feed_back = convert_main(opt, arg)
    console = Console()
    console.print(f'=' * os.get_terminal_size()[0], justify='center')
    console.print(f'[bold {color}]{feed_back}[/]', justify='center')
    console.print(f'=' * os.get_terminal_size()[0], justify='center')
