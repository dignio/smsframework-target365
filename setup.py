#! /usr/bin/env python
""" SMS framework: Target365 provider """

from setuptools import setup, find_packages

setup(
    # http://pythonhosted.org/setuptools/setuptools.html
    name='smsframework-target365',
    version='0.0.2-0',
    author='Ilya Vihtinsky',
    author_email='iliaviht@gmail.com',

    url='https://github.com/vihtinsky/py-smsframework-target365',
    license='BSD',
    description=__doc__,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['sms', 'message', 'notification', 'receive', 'send', 'target365'],

    packages=find_packages(),
    scripts=[],
    entry_points={},

    install_requires=[
        'smsframework >= 0.0.9',
        'target365-sdk >= 1.4.4'
    ],
    extras_require={
        'receiver': ['flask >= 0.10'],  # sms receiving
    },
    test_suite='nose.collector',
    include_package_data=True,

    platforms='any',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
)
