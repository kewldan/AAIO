# AAIO API for Python 3

<div align="center">

<a href="https://aaio.so/" target="_blank">
	<img alt="AAIO Badge" src="https://aaio.so/assets/svg/banners/big/dark-2.svg" title="Aaio - Сервис по приему онлайн платежей">
</a>

[![kewldan - AAIO](https://img.shields.io/static/v1?label=kewldan&message=AAIO&color=blue&logo=github)](https://github.com/kewldan/AAIO "Go to GitHub repo")
[![GitHub release](https://img.shields.io/github/release/kewldan/AAIO?include_prereleases=&sort=semver&color=blue)](https://github.com/kewldan/AAIO/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Upload Python Package](https://github.com/kewldan/AAIO/actions/workflows/python-publish.yml/badge.svg)](https://github.com/kewldan/AAIO/actions/workflows/python-publish.yml)
[![issues - AAIO](https://img.shields.io/github/issues/kewldan/AAIO)](https://github.com/kewldan/AAIO/issues)

[AAIO Official documentation](https://wiki.aaio.so/)

</div>

## About

This library is a wrapper for the https://aaio.so API **from enthusiasts**. All methods are described and all types are
**explicitly** defined. Methods that create requests to
aaio.so
return a pydantic's models for each response. Please write about all problems related to the library
to [issues](https://github.com/kewldan/AAIO/issues)

API is up-to-date as of *19 December 2023*.

* PyPl - https://pypi.org/project/aaio/
* Github - https://github.com/kewldan/AAIO
* Docs - https://kewldan.vercel.app/projects/aaio
* Demo - https://t.me/aaio_demo_bot
* Requirements: Python >= 3.7
* Added to [AAIO SDKs](https://wiki.aaio.so/priem-platezhei/gotovye-cms-moduli-i-sdk/python-3-sdk)

### Features

* It's completely **asynchronous**
* You can use **multiple** clients to work with **multiple** users or shops
* **All methods** for working with API are implemented
* The library returns strictly typed for responses from APIs
* For each method, **docstrings** are used
* The library handle {type: error} responses and throws AAIOBadRequest exception
* Our library was the **first** to be added to the **official** AAIO wiki
* **Modern**, strict code for Python 3.7

## Library Installation

* Install via pip: `pip install aaio`
* Download sources - `git clone https://github.com/kewldan/AAIO`

## Getting Started

### Get user balance

```python
import asyncio

from aaio import AAIO


async def main():
    client = AAIO('MERCHANT ID', 'SECRET KEY', 'API KEY')
    balances = await client.get_balances()
    print(balances)  # type='success' code=None message=None balance=625.85 referral=172.96 hold=0.0


asyncio.run(main())
```

### Create payment URL for customer

```python
import asyncio

from aaio import AAIO


async def main():
  client = AAIO('MERCHANT ID', 'SECRET KEY', 'API KEY')
  payment_url = client.create_payment(100, 'my_order_id', 'My order description', 'qiwi', 'support@aaio.so',
                                      'referral code', currency='USD',
                                      language='en')
  print(payment_url)  # Prints payment url for customer


asyncio.run(main())
```

### Create payoff

```python
import asyncio

from aaio import AAIO


async def main():
  client = AAIO('MERCHANT ID', 'SECRET KEY', 'API KEY')
  payoff = await client.create_payoff('qiwi', 100.35, '79998887766', 'my_payoff_id')
  print(payoff.status)  # in_progress


asyncio.run(main())
```

## Contact

E-Mail - kewldanil1@gmail.com
Telegram - [@kewldan](https://t.me/kewldan)

## License

Released under [MIT](/LICENSE) by [@kewldan](https://github.com/kewldan).
