#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""例題プログラム
"""

__author__ = '{{cookiecutter.author}}'
__version__ = '{{cookiecutter.version}}'
__date__ = '{{cookiecutter.date}}'

from test.support import captured_stdout
from {{cookiecutter.project_name}} import example


def test_example():
    """例題プログラムのテスト（標準出力）
    """
    with captured_stdout() as stdout:
        example.main()
        lines = stdout.getvalue().splitlines()
    assert "hello" == lines[0]
