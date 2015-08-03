#!/usr/bin/env python

import setuptools

try:
    import multiprocessing
except ImportError:
    pass


setuptools.setup(
    setup_requires=['pbr'],
    pbr=True
)

"""
setup(
    name=PROJECT,
    version=VERSION,

    description='Demo app for tests',

    author='Gobin Sougrakpam',
    packages=['redditcli'],


    entry_points={
        'console_scripts': [
            'redditcli = redditcli.main:main'
        ],
        'redditcli.tests': [
            'list = redditcli.list:Files',
        ],
    },

    zip_safe=False,
)
"""