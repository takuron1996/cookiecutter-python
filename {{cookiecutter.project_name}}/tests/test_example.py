#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム
"""

__author__ = '{{cookiecutter.author}}'
__version__ = '{{cookiecutter.version}}'
__date__ = '{{cookiecutter.date}}'

import textwrap
import os
from test.support import captured_stdout, captured_stdin
from {{cookiecutter.project_name}} import example


def test_example1():
    """例題プログラムのテスト1
    """
    input_value = textwrap.dedent("""\
        72
        128 256
        myonmyon""")
    output_value = textwrap.dedent("""\
        456 myonmyon""")
    run(input_value, output_value)


def test_example2():
    """例題プログラムのテスト2
    """
    input_value = textwrap.dedent("""\
        1
        2 3
        test""")
    output_value = textwrap.dedent("""\
        6 test""")
    run(input_value, output_value)


def run(input_value, output_value):
    """テスト実行（標準入力、標準出力）
    """
    with captured_stdout() as stdout, captured_stdin() as stdin:
        stdin.write(input_value)
        stdin.seek(0)
        example.main()
        lines = stdout.getvalue().splitlines()
    assert output_value == os.linesep.join(lines)
