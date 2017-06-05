#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

test_requirements = []

setup(
    author_email='sfischer13@ymail.com',
    author='Stefan Fischer',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
    description='Generator for random text that looks like Latin.',
    include_package_data=True,
    install_requires=requirements,
    keywords='lorem ipsum random text placeholder',
    license='MIT',
    long_description=readme + '\n\n' + history,
    name='lorem',
    package_dir={'lorem': 'lorem'},
    packages=['lorem'],
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sfischer13/python-lorem',
    version='0.1.1',
    zip_safe=False)
