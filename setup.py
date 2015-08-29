# -*- coding: utf-8 -*-
# All thanks to .../hr_python
from setuptools import setup

version = '0.1'

setup(
    name='hr',
    version=version,
    description='Horizontal rule for your terminal, with WRITTEN TASK NAME, to have a well-written problem statement before getting to console',
    author='Sumit murari',
    url='http://www.github.com/sumit007/hr_',
    license='',
    py_modules=['hr_'],
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    hr = hr_:cli
    """,
    )
