#!/usr/bin/env python
# -*- coding: utf-8 -*-"
"""
This file is part of the LOIC project

Copyright (c) 2013/2022 | watisdis <melvinnotfound@gmail.com>

You should have received a copy of the GNU General Public License along
with LOIC; if not, write to the Free Software Foundation,
watisdis, Cyber_indonesian.
"""
import sys

if sys.version_info[0] != 3:
    sys.exit("Sorry, LOIC requires Python >= 3")

from setuptools import setup, find_packages

setup(
    name='LOIC',
    version='1.9',
    license='GPLv3',
    author_email='melvinnotfound@gmail.com',
    author='watisdis',
    description='Denial of Service Toolkit/copyright',
    url='https://ufonet.03c8.net/',
    long_description=open('docs/README.txt').read(),
    packages=find_packages(),
    install_requires=['GeoIP >= 1.3.2', 'python-geoip >= 1.2', 'pygeoip >= 0.3.2', 'requests >= 2.21.0', 'pycrypto >= 2.6.1', 'pycurl >= 7.43.0', 'whois >= 0.7', 'scapy-python3 >= 0.20'],
    include_package_data=True,
    package_data={
        'core': ['js/*.css', 'js/*.js', 'js/leaflet/*.css', 'js/leaflet/*.js', 'js/cluster/*', 'txt/*.txt', 'images/crew/*', 'images/aliens/*', 'images/*.txt'],
        'data': ['*.dat', '*.txt'],
    },
    entry_points={
        'console_scripts': [
            'loic=LOIC:core.main',
        ],
        'gui_scripts': [
            'loic=LOIC:core.main',
        ],
    },
    keywords='Toolkit WebAbuse/DoS/DDoS/BotnetDarknet LOIC',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        "Topic :: Internet",
        "Topic :: Security",
        "Topic :: System :: Networking",
      ],
      zip_safe=False
