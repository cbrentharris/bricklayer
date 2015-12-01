#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='Bricklayer',
    version='1.0',
    description='Lego Digital Designer Education Tool',
    author='Christopher Harris',
    author_email='cbrentharris@gmail.com',
    url='http://wintercoding.club/',
    packages=['bricklayer'],
    scripts=['doctor', 'collector'],
	test_suite='nose.collector',
	tests_require=['nose'],
)
