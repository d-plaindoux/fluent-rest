# Copyright (C)2016 D. Plaindoux.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2, or (at your option) any
# later version.

from setuptools import setup

setup(
    name='fluent-rest',
    version='0.1',
    packages=['fluent_rest'],
    url='https://github.com/d-plaindoux/fluent-rest',
    license='LGPL ',
    author='d-plaindoux',
    author_email='d.plaindoux@free.fr',
    keywords='REST WSGI decorators a la JAX-RS',
    description='decorators for seamless REST library specification',
    test_suite="tests"
)
