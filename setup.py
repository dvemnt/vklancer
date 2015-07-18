# -*- coding: utf-8 -*-

from os import path
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '1.0.0'

packages = [
    'vklancer'
]

requires = [
    'requests'
]

here = path.abspath(path.dirname(__file__))

try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

setup(
    name='vklancer',
    version=VERSION,
    packages=packages,
    requires=requires,
    description='Simple using vk.com API.',
    long_description=long_description,
    author='Vitalii Maslov',
    author_email='me@pyvim.com',
    url='https://github.com/pyvim/vklancer',
    download_url='https://github.com/pyvim/vklancer/tarball/master',
    license='MIT',
    keywords = 'vk.com, API, vklancer',
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)
