[![GitHub Release](https://img.shields.io/github/release/LUCIT-Systems-and-Development/unicorn-trading-suite.svg?label=github)](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/LUCIT-Systems-and-Development/unicorn-trading-suite/total?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/releases)
![Anaconda Release](https://img.shields.io/conda/v/lucit/unicorn-trading-suite?color=blue)
![Anaconda Downloads](https://img.shields.io/conda/dn/lucit/unicorn-trading-suite?color=blue)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-trading-suite?color=blue)](https://pypi.org/project/unicorn-trading-suite/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-trading-suite)](https://pepy.tech/project/unicorn-trading-suite)
[![License](https://img.shields.io/badge/license-LSOSL-blue)](https://unicorn-trading-suite.docs.lucit.tech/license.html)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_trading_suite.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_trading_suite.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/issues)
[![Unit Tests](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/actions/workflows/unit-tests.yml)
[![Build and Publish GH+PyPi](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/actions/workflows/build_wheels.yml)
[![Build and Publish Anaconda](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/actions/workflows/build_conda.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/actions/workflows/build_conda.yml)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://unicorn-trading-suite.docs.lucit.tech/)
[![Read How To`s](https://img.shields.io/badge/read-%20howto-yellow)](https://medium.lucit.tech)
[![GitHub](https://img.shields.io/badge/source-github-cbc2c8)](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite)
[![Telegram](https://img.shields.io/badge/community-telegram-41ab8c)](https://t.me/unicorndevs)
[![Get Free Professional Support](https://img.shields.io/badge/chat-lucit%20support-004166)](https://www.lucit.tech/get-support.html)

# UNICORN Trading Suite
[Description](#description) | [Installation](#installation-and-upgrade) | [How To](#howto) | [Change Log](#change-log) | 
[Documentation](#documentation) | [Social](#social) | [Notifications](#receive-notifications) | [Bugs](#how-to-report-bugs-or-suggest-improvements) | 
[Contributing](#contributing) | [Disclaimer](#disclaimer) | [Commercial Support](#commercial-support)

## Description
LUCIT's [`UNICORN Trading Suite`](https://www.lucit.tech/unicorn-trading-suite.html) is a comprehensive collection of open-source Python packages designed for 
building sophisticated automated trading systems. Tailored for Python developers, this suite offers seamless 
integration with various crypto exchange APIs, enabling the creation of advanced and professional trading bots for 
streamlined and efficient cryptocurrency trading.

All libraries in the suite are coordinated with each other, interlock perfectly, are fully documented and offer 
standardized interfaces and tools for the programmer. LUCIT continuously develops the modules, fixes bugs, tests the 
libraries extensively and offers [fast, direct and free support](https://www.lucit.tech/get-support.html).

All modules are delivered optimized as PyPy and as Python C Extension (Cython) via 
[PyPi](https://pypi.org/user/LUCIT/) and [Anaconda](https://anaconda.org/lucit). The package 
creation runs completely transparently directly from the respective GitHub repository through GitHub Actions and is 
deployed directly to PyPi and Anaconda in a traceable manner. This process makes it tamper-proof for you to 
understand which code is contained in which package and can therefore easily install optimized builds for the platform, 
architecture and Python version used.

[Get help](https://www.lucit.tech/get-support.html) with the integration of the `UNICORN Trading Suite` modules!

## Modules of the UNICORN Trading Suite
We currently only offer full support for Binance. However, we have started to integrate other top 10 exchanges 
(ByBit, HTX, ...). Step by step we will be able to announce new support here!

### [UNICORN Trading Suite for Binance](https://www.lucit.tech/unicorn-binance-suite.html)
- [`UNICORN Binance Local Depth Cache`](https://www.lucit.tech/unicorn-binance-local-depth-cache.html): A Python SDK 
  from LUCIT to access and manage multiple local Binance DepthCaches with Python in a simple, fast, flexible, robust 
  and fully-featured way. 
- [`UNICORN Binance REST API`](https://www.lucit.tech/unicorn-binance-rest-api.html): A Python SDK by LUCIT to use the Binance REST API`s (com+testnet, 
  com-margin+testnet, com-isolated_margin+testnet, com-futures+testnet, us, tr) in a simple, fast, flexible, robust 
  and fully-featured way. 
- [`UNICORN Binance Trailing Stop Loss`](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html): A Python SDK and [Command Line Tool](https://www.lucit.tech/ubtsl-cli.html) 
  from LUCIT with a trailing stop loss engine for the Binance Exchanges.
- [`UNICORN Binance WebSocket API`](https://www.lucit.tech/unicorn-binance-websocket-api.html): A Python SDK by LUCIT to use the Binance Websocket API`s (com+testnet, 
  com-margin+testnet, com-isolated_margin+testnet, com-futures+testnet, com-coin_futures, us, tr, dex/chain+testnet) in 
  a simple, fast, flexible, robust and fully-featured way. 
- [`UnicornFy`](https://www.lucit.tech/unicorn-fy.html): A Python SDK by LUCIT to convert received raw data from crypto exchange API endpoints into 
  well-formed python dictionaries. 

### UNICORN Trading Suite for ByBit
- [`UNICORN ByBit WebSocket API`](https://www.lucit.tech/unicorn-bybit-websocket-api.html): A Python SDK by LUCIT to use 
  the ByBit Websocket API`s in a simple, fast, flexible, robust and fully-featured way. 

If you like our projects, please 
[![star](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-trading-suite/master/images/misc/star.png)](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/stargazers) them on 
[GitHub](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite)! 

## Get a UNICORN Trading Suite License

To run modules of the *UNICORN Trading Suite* you need a [valid license](https://medium.lucit.tech/how-to-obtain-and-use-a-unicorn-trading-suite-license-key-and-run-the-ubs-module-according-to-best-87b0088124a8#4ca4)!

## UNICORN Trading Suite comparison
It is not easy to choose the right Python library to build your trading system. With this table we would like to help 
you get an objective overview and simplify the selection of the right package:

| **Feature/Criteria**                  | **Binance Connector**                                                    | **python-binance**                                                          | **UNICORN Trading Suite**                                                                                 | **CCXT/CCXT Pro**                                                             |
|---------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **REST API Support**                  | Yes, full support                                                        | Yes, full support                                                           | Yes, full support                                                                                         | Yes, supports REST for Binance and many other exchanges                       |
| **WebSocket Streams**                 | Yes, including new WebSocket trading API for orders and trading commands | Yes, for market data and user data streams                                  | Yes, including new WebSocket trading API for orders and trading commands and advanced management features | Yes, CCXT Pro                                                                 | 
| **Stream Signals**                    | Not available                                                            | Not available                                                               | Yes                                                                                                       | Not available                                                                 | 
| **Trading via WebSocket**             | Yes                                                                      | No, REST API only                                                           | Yes, via UBWA, specifically developed and maintained by LUCIT                                             | Yes, CCXT Pro                                                                 |
| **Asynchronous Processing**           | Yes, supports async functions                                            | Partially, limited support                                                  | Yes, full `asyncio` integration in UBWA and UBLDC                                                         | Yes, supports async functions                                                 |
| **Official Support**                  | Yes, official Binance project                                            | No, community-driven                                                        | No, but continuously maintained and supported by LUCIT                                                    | No, community-driven                                                          |
| **Maintenance and Updates**           | Regular updates and maintenance by Binance                               | Depends on community contributions                                          | Regular updates by LUCIT, quickly adapting to API changes                                                 | Regular updates, dependent on community and external exchanges                |
| **UnicornFy Data Formatting**         | Not available                                                            | Not available                                                               | Yes, via UnicornFy for consistent data structuring, developed by LUCIT                                    | Not available                                                                 |
| **Depth Caches (Order Book Storage)** | Basic depth via WebSocket available                                      | Includes a basic depth cache manager but may be limited for advanced needs. | Yes, UBLDC provides specialized management for order book depth, developed by LUCIT                       | CCXT Pro: Basic depth via WebSocket available, without specialized management |
| **Depth Cache Cluster**               | Not available                                                            | Not available                                                               | Yes, via UNICORN DepthCache Cluster for Binance with Load Balancing and Failover                          | Not available                                                                 |
| **Trailing Stop-Loss**                | Not natively, only manually via REST                                     | Not natively, only manually via REST                                        | Yes, via Trailing Stop Order module, automated, maintained by LUCIT                                       | Not natively supported, only manually via REST                                |
| **Multi-Exchange Support**            | Binance only                                                             | Binance only                                                                | Binance, Bybit, and top exchanges in progress                                                             | Yes, supports multiple exchanges                                              |
| **Configuration Complexity**          | Simple, unified configuration                                            | Simple, unified configuration                                               | Modular, each component can be selectively deployed                                                       | Simple, unified configuration                                                 |
| **Community and Support**             | Official support from Binance                                            | Large community support                                                     | Specialized community and support (SLA), continuous development by LUCIT                                  | Large, active community                                                       |
| **Available as C-Extension**          | Not available                                                            | Not available                                                               | Yes, the entire stack is available as a compiled Python C extension on PyPi and Anaconda                  | Not available                                                                 |
| **Compatible with PyPy**              | Not available                                                            | Not available                                                               | Yes, the entire stack is available as a PyPy package on PyPi                                              | Not available                                                                 |
| **Ideal For**                         | Developers looking for an officially supported library                   | General Binance applications and REST trading                               | High-frequency trading with advanced features, advanced order book processing, multi-asset monitoring     | Multi-exchange trading and data querying via a unified API                    |


## Installation and Upgrade

The modules require Python 3.8 or above, as they depend on Pythons latest asyncio features for asynchronous/concurrent 
processing. 

For the PyPy interpreter we offer packages only from Python version 3.9 and higher.

Anaconda packages are available from Python version 3.8 and higher.

If you run into errors during the installation take a look [here](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/wiki/Installation).

### Packages are created automatically with GitHub Actions
When a new release is to be created, we start two GitHubActions: 

- [Build and Publish Anaconda](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/actions/workflows/build_conda.yml)
- [Build and Publish GH+PyPi](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/actions/workflows/build_wheels.yml) 

Both start virtual Windows/Linux/Mac servers provided by GitHub in the cloud with preconfigured environments and 
create the respective compilations and stub files, pack them into wheels and conda packages and then publish them on 
GitHub, PYPI and Anaconda. This is a transparent method that makes it possible to trace the source code behind a 
compilation.

### A Cython binary, PyPy or source code based CPython wheel of the latest version with `pip` from [PyPI](https://pypi.org/project/unicorn-binance-rest-api/)
Our [Cython](https://cython.org/) and [PyPy](https://www.pypy.org/) Wheels are available on [PyPI](https://pypi.org/), 
these wheels offer significant advantages for Python developers:

- ***Performance Boost with Cython Wheels:*** Cython is a programming language that supplements Python with static 
  typing and C-level performance. By compiling Python code into C, Cython Wheels can significantly enhance the 
  execution speed of Python code, especially in computationally intensive tasks. This means faster runtimes and more 
  efficient processing for users of our package. 

- ***PyPy Wheels for Enhanced Efficiency:*** PyPy is an alternative Python interpreter known for its speed and 
  efficiency. It uses Just-In-Time (JIT) compilation, which can dramatically improve the performance of Python code. 
  Our PyPy Wheels are tailored for compatibility with PyPy, allowing users to leverage this speed advantage seamlessly.

Both Cython and PyPy Wheels on PyPI make the installation process simpler and more straightforward. They ensure that 
you get the optimized version of our package with minimal setup, allowing you to focus on development rather than 
configuration.

#### Installation
`pip install unicorn-trading-suite`

#### Update
`pip install unicorn-trading-suite --upgrade`

### A Conda Package of the latest version with `conda` from [Anaconda](https://anaconda.org/lucit)
The `unicorn-trading-suite` package is also available as a Cython version for the `linux-64`, `osx-64` 
and `win-64` architectures with [Conda](https://docs.conda.io/en/latest/) through the 
[`lucit` channel](https://anaconda.org/lucit). 

For optimal compatibility and performance, it is recommended to source the necessary dependencies from the 
[`conda-forge` channel](https://anaconda.org/conda-forge). 

#### Installation
```
conda config --add channels conda-forge
conda config --add channels lucit
conda install -c lucit unicorn-trading-suite
```

#### Update
`conda update -c lucit unicorn-trading-suite`

### From source of the latest release with PIP from [GitHub](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite)
#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/archive/$(curl -s https://api.github.com/repos/LUCIT-Systems-and-Development/unicorn-trading-suite/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`

#### Windows
Use the below command with the version (such as 1.0.0) you determined 
[here](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/releases/latest):

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/archive/1.0.0.tar.gz --upgrade`

### From the latest source (dev-stage) with PIP from [GitHub](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://www.python.org)
Download the [latest release](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/releases/latest) 
or the [current master branch](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/archive/master.zip)
 and use:
 
- ./environment.yml
- ./pyproject.toml
- ./requirements.txt
- ./setup.py

## Change Log
[https://unicorn-trading-suite.docs.lucit.tech/changelog.html](https://unicorn-trading-suite.docs.lucit.tech/changelog.html)

Please look for the information in the README.md of the [responsible subrepository](https://www.lucit.tech/unicorn-trading-suite.html#modules-of-the-unicorn-trading-suite).

## Documentation
- [General](https://unicorn-trading-suite.docs.lucit.tech/)

Please look for the information in the README.md of the [responsible subrepository](https://www.lucit.tech/unicorn-trading-suite.html#modules-of-the-unicorn-trading-suite).

## Howto
- [How to Obtain and Use a UNICORN Trading Suite License Key and Run the UBS Module According to Best Practice](https://medium.lucit.tech/how-to-obtain-and-use-a-unicorn-trading-suite-license-key-and-run-the-ubs-module-according-to-best-87b0088124a8)
- [Instructions about the UNICORN Trading Suite](https://medium.lucit.tech/unicorn-trading-suite/home)

## Project Homepage
[https://www.lucit.tech/unicorn-trading-suite.html](https://www.lucit.tech/unicorn-trading-suite.html)

## Wiki
[https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/wiki](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/wiki)

## Social
- [Discussions](https://github.com/LUCIT-Systems-and-Development/unicorn-trading-suite/discussions)
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://community.binance.org](https://community.binance.org)

## Receive Notifications
Follow us on [LinkedIn](https://www.linkedin.com/company/lucit-systems-and-development), 
[X](https://twitter.com/LUCIT_SysDev) or [Facebook](https://www.facebook.com/lucit.systems.and.development)!

Please look for the information in the README.md of the [responsible subrepository](https://www.lucit.tech/unicorn-trading-suite.html#modules-of-the-unicorn-trading-suite) for spezific notifications.

## How to report Bugs or suggest Improvements?
Please look for the information in the README.md of the [responsible subrepository](https://www.lucit.tech/unicorn-trading-suite.html#modules-of-the-unicorn-trading-suite).

## Contributing
Please look for the information in the README.md of the [responsible subrepository](https://www.lucit.tech/unicorn-trading-suite.html#modules-of-the-unicorn-trading-suite).

## Disclaimer
This project is for informational purposes only. You should not construe this information or any other material as 
legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, 
endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in 
this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such 
jurisdiction.

### If you intend to use real money, use it at your own risk!

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities 
of any kind, including but not limited to direct or indirect damages for loss of profits.

### SOCKS5 Proxy / Geoblocking
We would like to explicitly point out that in our opinion US citizens are exclusively authorized to trade on Binance.US 
and that this restriction must not be circumvented!

The purpose of supporting a SOCKS5 proxy in the UNICORN Trading Suite and its modules is to allow non-US citizens to 
use US services. For example, GitHub actions with UBS will not work without a SOCKS5 proxy, as they will inevitably run 
on servers in the US and be blocked by Binance.com. Moreover, it also seems justified that traders, data scientists and 
companies from the US analyze binance.com market data - as long as they do not trade there.

## Commercial Support

[![Get professional and fast support](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-trading-suite/master/images/support/LUCIT-get-professional-and-fast-support.png)](https://www.lucit.tech/get-support.html)

***Do you need a developer, operator or consultant?*** [Contact us](https://www.lucit.tech/contact.html) for a non-binding initial consultation!
