#!/usr/bin/env python

PROJECT = 'redditcli'
VERSION = '0.1'

from setuptools import setup, find_packages

try:
	long_description = open('README.rst', 'rt').read()
except IOError:
	long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Demo app for test',

    author='Gobin Sougrakpam',


    entry_points={
        'console_scripts': [
            'redditcli = redditcli.main:main'
        ],
        'redditcli.test': [
            'list = redditcli.list:Files',
        ],
    },

    zip_safe=False,
)

"""
setup(
    name=PROJECT,
    version=VERSION,

    description='Python app for calling Reddit API',

    author='Gobin Sougrakpam',
    author_email='gobin.sougrakpam@gmail.com',

    url='https://github.com/gobins/python-reddit-api',
    platform=['Any']







	)

"""