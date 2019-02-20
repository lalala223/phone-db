# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

NAME = 'phone-db'
DESCRIPTION = '手机号码SQLite数据库'
AUTHOR = 'lalala223'
AUTHOR_EMAIL = 'hi@lalala.ink'
URL = 'https://github.com/lalala223/phone-db'
VERSION = '1.0.3'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license='MIT',
    url=URL,
    include_package_data=True,
    install_requires=['sqlalchemy'],
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    zip_safe=False,
)
