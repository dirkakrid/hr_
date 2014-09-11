# -*- coding: utf-8 -*-
# All thanks to .../hr_python 
from setuptools import setup

version = '0.1'

setup(
    name='hr',
    version=version,
    description='Horizontal rule for your terminal, with WRITTEN TASK NAME, to not let you distracted',
    author='Sumit murari',
    url='https://www.github.com/sumit007/hr_',
    license='',
    py_modules=['hr'],
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    hr = hr:cli
    """,
    )
