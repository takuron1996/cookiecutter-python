#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム
"""

__author__ = '{{cookiecutter.author}}'
__version__ = '{{cookiecutter.version}}'
__date__ = '{{cookiecutter.date}}'


def main():
    """提出プログラム
    """
    a = int(input())
    b, c = tuple(map(int, input().split()))
    s = input()

    print(f"{a + b + c} {s}")


if __name__ == "__main__":

    main()
