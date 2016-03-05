#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.export.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(
    name='mapzen.whosonfirst.brands.export',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.brands', 'mapzen.whosonfirst.brands.export'],
    version=version,
    description='Simple Python wrapper for managing Who\'s On First export-related functions',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-export',
    install_requires=[
        'geojson',
        'atomicwrites',
        'mapzen.whosonfirst.brands.utils>=0.01',
        ],
    dependency_links=[
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-brands-utils/tarball/master#egg=mapzen.whosonfirst.brands.utils-0.01',
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-brands-export/releases/tag/' + version,
    license='BSD')
