#!/usr/bin/python
# -*- coding:Utf-8 -*-

# Beuarg - an OpenERP code puker
# Copyright (C) 2013 Laurent Peuch <cortex@worlddomination.be>
#                    Railnova SPRL <railnova@railnova.eu>
#
# This file is part of Beuarg.
#
# Beuarg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# Beuarg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Beuarg.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

setup(name='Beuarg',
      version='0.1',
      description='OpenERP code puker',
      author='Laurent Peuch',
      long_description=open("README.rst").read(),
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/beuarg',
      install_requires=['argh', 'argcomplete', 'vodka'],
      packages=['beuarg'],
      license= 'GPLv3+',
      scripts=['bin/beuarg'],
      keywords='openerp,code generator',
     )
