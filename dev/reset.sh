#!/usr/bin/bash

rm *.log
rm dev/*.log

rm build -r
rm dist -r
rm *.egg-info -r

rm unicorn_trading_suite/*.c
rm unicorn_trading_suite/*.html
rm unicorn_trading_suite/*.dll
rm unicorn_trading_suite/*.so

rm .print_summary.txt