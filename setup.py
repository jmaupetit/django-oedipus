#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-oedipus',
    version='0.1',
    url='',
    author='Julien Maupetit',
    author_email='julien@maupetit.net',
    description='Integrate sphinx documentations to your django projects',
    long_description=open('README.md').read(),
    keywords="Sphinx, Django, Documentation",
    license='BSD',
    platforms=['all'],
    packages=find_packages(),
    include_package_data = True,
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Environment :: Web Environment',
             'Framework :: Django',
             'Intended Audience :: Developers',
             'License :: OSI Approved :: BSD License',
             'Operating System :: Unix',
             'Programming Language :: Python'],
    install_requires=[],
    )
