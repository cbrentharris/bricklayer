#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='Bricklayer',
    version='1.0',
    description='Lego Digital Designer Education Tool',
    author='Christopher Harris',
    author_email='cbrentharris@gmail.com',
    url='http://wintercoding.club/',
    packages=find_packages(),
    entry_points = {
        'console_scripts' : [
            'bricklayer = bricklayer:main'
        ]
    },
    test_suite='nose.collector',
    tests_require=['nose'],
)
