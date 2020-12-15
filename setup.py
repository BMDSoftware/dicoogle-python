# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
dicoogle-python - dicoogle API client for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**dicoogle-python** is the official Python client for the dicoogle API.

:copyright: (c) 2020, Luís A. Bastião Silva, BMD Software
:license: MIT

'''


import sys
from distutils.core import setup


if sys.version_info < (2, 7):
    raise NotImplementedError('Sorry, you need Python 2.7 or '
                              'Python 3.x to use `dicoogle-python`.')

setup(name='dicoogle',
      version='1.0',
      description='dicoogle API client for Python.',
      long_description=__doc__,
      author='Luis Bastião Silva',
      author_email='bastiao@bmd-software.com',
      license='CC-BY-NC',
      install_requires=['requests>=1.2.0'],
      py_modules=['dicoogle'],
      scripts=['dicoogle.py'],
      platforms='any',
      classifiers=[
          'Intended Audience :: Science/Research',
          'Intended Audience :: Developers',
          'Topic :: Software Development',
          'Topic :: Scientific/Engineering',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7'],
      )
