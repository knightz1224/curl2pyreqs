#!/bin/env python3
import argparse


def main(**kwargs):
    sys_parser = argparse.ArgumentParser()
    sys_parser.add_argument('-f', '--file')
    sys_parser.add_argument('-c', '--clean', action='store_true')
    sys_args = sys_parser.parse_args()
    # print(sys_args)
    from .common import main
    main(file=sys_args.file, clean=sys_args.clean)


if __name__ == '__main__':
    main()
