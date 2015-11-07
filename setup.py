#!/usr/bin/env python

from distutils.core import setup

setup(name='Bricklayer',
    version='1.0',
    description='Lego Digital Designer Education Tool',
    author='Christopher Harris',
    author_email='cbrentharris@gmail.com',
    url='http://wintercoding.club/',
    packages=['distutils', 'distutils.command'],
    scripts=['doctor']
)
