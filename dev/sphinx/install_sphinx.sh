#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/sphinx/install_sphinx.sh
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

python3 -m pip install sphinx --upgrade
python3 -m pip install python-docs-theme-lucit --upgrade
python3 -m pip install rich --upgrade
python3 -m pip install myst-parser --upgrade
python3 -m pip install sphinx-markdown-tables --upgrade