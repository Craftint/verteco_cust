# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in verteco_cust/__init__.py
from verteco_cust import __version__ as version

setup(
	name='verteco_cust',
	version=version,
	description='Customisations',
	author='Dany Robert',
	author_email='rtdany10@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
