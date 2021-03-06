#!/usr/bin/env python

from setuptools import setup

setup(name='ida-settings',
      version="0.2",
      description="Fetch and set configuration values in IDA Pro IDAPython scripts",
      author='Willi Ballenthin',
      author_email='william.ballenthin@fireeye.com',
      url='https://github.com/williballenthin/ida-settings',
      license='Apache License (2.0)',
      packages=['ida_settings'],
      classifiers = ["Programming Language :: Python",
                     "Programming Language :: Python :: 2",
                     "Operating System :: OS Independent",
                     "License :: OSI Approved :: Apache Software License"],
     )
