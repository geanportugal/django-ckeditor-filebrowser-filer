#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import ckeditor_filebrowser_filer

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = ckeditor_filebrowser_filer.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print('You probably want to also tag the version now:')
    print('  git tag -a %s -m \'version %s\'' % (version, version))
    print('  git push --tags')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-ckeditor-filebrowser-filer',
    version=version,
    description='A django-filer based CKEditor filebrowser',
    long_description=readme + '\n\n' + history,
    author='Iacopo Spalletti',
    author_email='i.spalletti@nephila.it',
    url='https://github.com/nephila/django-ckeditor-filebrowser-filer',
    packages=[
        'ckeditor_filebrowser_filer',
    ],
    include_package_data=True,
    install_requires=[
        'django-filer>=1.0',
    ],
    license='BSD',
    zip_safe=False,
    keywords='django-ckeditor-filebrowser-filer, django, filer, ckeditor, filebrowser',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)