#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘UNICORN Trading Suite’
# Project website: https://www.lucit.tech/unicorn-trading-suite.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite
# Documentation: https://unicorn-trading-suite.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-trading-suite
# LUCIT Online Shop: https://shop.lucit.services/software
#
# License: LSOSL - LUCIT Synergetic Open Source License
# https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/blob/master/LICENSE
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2023, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='unicorn_trading_suite',
     version='1.0.0',
     author="LUCIT Systems and Development",
     author_email='info@lucit.tech',
     url="https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite",
     description="LUCIT's UNICORN Trading Suite is a comprehensive collection of open-source Python packages designed "
                 "for building sophisticated automated trading systems. Tailored for Python developers, this suite "
                 "offers seamless integration with the Binance API, enabling the creation of advanced and professional "
                 "trading bots for streamlined and efficient cryptocurrency trading.",
     long_description=long_description,
     long_description_content_type="text/markdown",
    license='LSOSL - LUCIT Synergetic Open Source License',
     install_requires=['unicorn-binance-suite', 'unicorn-bybit-websocket-api', 'lucit-backtesting'],
     keywords='UNICORN Trading Suite, LUCIT, LUCIT Systems and Development',
     project_urls={
        'Documentation': 'https://unicorn-trading-suite.docs.lucit.tech/',
        'Changes': 'https://unicorn-trading-suite.docs.lucit.tech/changelog.html',
        'License': 'https://unicorn-trading-suite.docs.lucit.tech/license.html',
        'Issue Tracker': 'https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/issues',
        'Wiki': 'https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/wiki',
        'Author': 'https://www.lucit.tech',
        'Telegram': 'https://t.me/unicorndevs',
        'Get Support': 'https://www.lucit.tech/get-support.html',
        'LUCIT Online Shop': 'https://shop.lucit.services/software',
     },
     python_requires='>=3.7.0',
     packages=find_packages(exclude=["tools", "images", "dev", "docs", ".github"]),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
         "Programming Language :: Python :: 3.11",
         "Programming Language :: Python :: 3.12",
         "Programming Language :: Python :: 3.13",
         "License :: Other/Proprietary License",
         'Intended Audience :: Developers',
         "Intended Audience :: Financial and Insurance Industry",
         "Intended Audience :: Information Technology",
         "Intended Audience :: Science/Research",
         "Operating System :: OS Independent",
         "Topic :: Office/Business :: Financial :: Investment",
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
)

