# -*- coding: utf-8 -*-
"""
:mod:`setup.py`
===============

.. module:: setup
   :platform: Unix, Windows
   :synopsis: The Python Packaging setup file for MINNs.

.. moduleauthor:: tibo <tibo@tibovanheule.space>

Created on 2015-11-05

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import re
from codecs import open
from setuptools import setup, find_packages, Extension

import numpy


def read(f):
    return open(f, encoding='utf-8').read()

setup(
    name='mil_nets',
    version='0.01',
    author='Henrik Blidh',
    author_email='henrik.blidh@nedomkull.com',
    url='https://github.com/tibovanheule/MINNs',
    description="Mi-net and mi-net algrorithms",
    long_description=read('README.md'),
    license='MIT',
    keywords=['Machine Learning', 'neural'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    packages=find_packages(exclude=[]),
    package_data={
        'mil_nets.stumps.ext': ['src/*', ],
        'mil_nets.datasets.musk': ['clean*.*', ],
    },
    install_requires=[
        'numpy',
        'scipy',
        'keras',
        'six',
        'psutil',
        'futures;python_version<"3.4"',
    ],
    dependency_links=[],
    ext_package='mil_nets.stumps.ext',
    ext_modules=[],
    entry_points={}
)

