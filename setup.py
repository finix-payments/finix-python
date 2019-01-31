#!/usr/bin/env python

from setuptools import setup

requirements = [
    'requests',
    'pilo',
    'iso8601',
]


setup(
    name='finix',
    version='1.0.18',
    url='https://github.com/finix-payments/finix-python',
    author='michael serna',
    author_email='michael@finixpayments.com',
    description='Finix payments API client library',
    packages=['finix'],
    include_package_data=True,
    install_requires=requirements,
    tests_require=['ipdb', 'nose'],
    test_suite='tests',
)
