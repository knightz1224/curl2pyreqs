#!/usr/bin/env python3

PROJECT_NAME = 'curl2pyreqs'
PACKAGE_NAME = 'curl2pyreqs'

import os
here = os.path.abspath(os.path.dirname(__file__))
proj_info = {
    "name":
    "curl2pyreqs",
    "version":
    "0.1.0",
    "author":
    "ZHANG HJ",
    "author_email":
    "kngihtz1224@163.com",
    "url":
    "https://github.com/knightz1224/curl2pyreqs",
    "license":
    "GPLv3",
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    "description":
    "A Library to Convert Curl to Python Requests File",
    "console_scripts": ["curl2pyreqs = curl2pyreqs.__main__:main"]
}
try:
    README = open(os.path.join(here, 'README.md'), encoding='utf-8').read()
except:
    README = ""

from setuptools import setup, find_packages
setup(name=proj_info['name'],
      version=proj_info['version'],
      author=proj_info['author'],
      author_email=proj_info['author_email'],
      url=proj_info['url'],
      license=proj_info['license'],
      description=proj_info['description'],
      classifiers=proj_info['classifiers'],
      long_description=README,
      long_description_content_type="text/markdown",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      platforms='any',
      zip_safe=True,
      entry_points={'console_scripts': proj_info['console_scripts']},
      python_requires=">=3.8")
