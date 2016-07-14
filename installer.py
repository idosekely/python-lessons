#!/usr/bin/python
import pip
__author__ = 'sekely'


packages = ['requests', 'pandas', 'numpy', 'flask', ]
print("this will install python lessons dependencies")

for package in packages:
    pip.main(['install', package])
