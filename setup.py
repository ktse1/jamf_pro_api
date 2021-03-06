#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'SQLAlchemy>=1.2.2',

    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(sreyemnayr): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='jssapi',
    version='0.1.2',
    description="Provide API calls for jamf Pro (formerly JSS)",
    long_description=readme + '\n\n' + history,
    author="Ryan Meyers",
    author_email='ryanmeyersweb@gmail.com',
    url='https://github.com/sreyemnayr/jamf_pro_api',
    packages=find_packages(include=['jssapi']),
    entry_points={
        'console_scripts': [
            'jssapi=jssapi.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='jssapi',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
