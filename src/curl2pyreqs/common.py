#!/bin/env python3
import os

from rich.console import Console

from .ulti import *


def main(**kwargs):
    color, feed_back = convert_main(**kwargs)
    if not kwargs['clean']:
        console = Console()
        console.print(f'=' * os.get_terminal_size()[0], justify='center')
        console.print(f'[bold {color}]{feed_back}[/]', justify='center')
        console.print(f'=' * os.get_terminal_size()[0], justify='center')
    else:
        if color != 'green':
            print(feed_back)
