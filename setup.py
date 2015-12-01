# coding=utf-8

from os import path
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '1.3.0'

packages = [
    'vklancer'
]

requires = [
    'requests'
]

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='vklancer',
    version=VERSION,
    packages=packages,
    install_requires=requires,
    description='Simple usage vk.com API.',
    long_description=long_description,
    author='Vitalii Maslov',
    author_email='me@pyvim.com',
    url='https://github.com/pyvim/vklancer',
    download_url='https://github.com/pyvim/vklancer/tarball/master',
    license='MIT',
    keywords='vk.com, API, vklancer',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)
