#!/usr/bin/env python
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


requires = [
'django',
'django-polymorphic',
'django-widget-tweaks',
'django-rest-framework',
'django-filter',
'djangorestframework-csv',
'django-rest-polymorphic',
'conllu',
'colour',
'pyexcel',
'pyexcel-xlsx',
'seqeval'
]

setup(
    name="django-doccano",
    version="0.1.0",
    packages=["doccano"],
    python_requires=">=3.8",
    include_package_data=True,
    install_requires=requires,
    license="MIT License",  # example license
    description="Django Specific doccano",
    long_description=README,
    url="https://github.com/ajbeach2/doccano",
    author="Alexander Beach",
    author_email="ajbeach2@gmail.com",
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :rm: 3.8",
    ],
)