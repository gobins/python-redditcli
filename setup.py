#!/usr/bin/env python

PROJECT = 'redditapicli'
VERSION = '0.1'

from setuptools import setup, find_packages

try:
	long_description = open('README.rst', 'rt').read()
except IOError:
	long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Python app for calling Reddit API'
    long_description=long_description,

    author='Gobin Sougrakpam',
    author_email='gobin.sougrakpam@gmail.com',

    url='https://github.com/gobins/python-reddit-api',
    platform=['Any']







	)