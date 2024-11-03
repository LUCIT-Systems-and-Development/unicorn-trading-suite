#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: unicorn_trading_suite/manager.py
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

import logging
from unicorn_binance_local_depth_cache import *
from unicorn_binance_rest_api import *
from unicorn_binance_trailing_stop_loss import *
from unicorn_binance_websocket_api import *
from unicorn_fy import *

__app_name__: str = "unicorn-trading-suite"
__version__: str = "2.0.0.dev"

logger = logging.getLogger("unicorn_trading_suite")


class BinanceSuite:
    def __init__(self):
        self.name = __app_name__
        self.version = __version__
        self.logger = logger
