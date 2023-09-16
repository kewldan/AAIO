# AAIO API for Python 3

<div align="center">

<a href="https://aaio.io/" target="_blank">
	<img src="https://aaio.io/assets/svg/banners/big/dark-2.svg" title="Aaio - Сервис по приему онлайн платежей">
</a>

[![kewldan - AAIO](https://img.shields.io/static/v1?label=kewldan&message=AAIO&color=blue&logo=github)](https://github.com/kewldan/AAIO "Go to GitHub repo")
[![GitHub release](https://img.shields.io/github/release/kewldan/AAIO?include_prereleases=&sort=semver&color=blue)](https://github.com/kewldan/AAIO/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Upload Python Package](https://github.com/kewldan/AAIO/actions/workflows/python-publish.yml/badge.svg)](https://github.com/kewldan/AAIO/actions/workflows/python-publish.yml)
[![issues - AAIO](https://img.shields.io/github/issues/kewldan/AAIO)](https://github.com/kewldan/AAIO/issues)

[AAIO Official documentation](https://wiki.aaio.io/)

</div>

## About

This library is a wrapper for the https://aaio.io API **from enthusiasts**. All methods are described and all types are
**explicitly** defined. The library does **not handle any exceptions**, so be careful. Methods that create requests to
aaio.io
return a pydantic's models for each response. Please write about all problems related to the library
to [issues](https://github.com/kewldan/AAIO/issues)

API is up-to-date as of *17 September 2023*.

* PyPl - https://pypi.org/project/aaio/
* Github - https://github.com/kewldan/AAIO
* Requirements: Python >= 3.7
* Added to [AAIO SDKs](https://wiki.aaio.io/priem-platezhei/gotovye-cms-moduli-i-sdk/python-3-sdk)

### Features

* It's completely **asynchronous**
* Uses single aiohttp session to improve **performance**
* You can use **multiple** clients to work with **multiple** users or shops
* **All methods** for working with API are implemented
* The library returns strictly typed for responses from APIs
* For each method, **docstrings** are used
* The library does not handle {type: error} responses, so you can do it **yourself**, which gives it **more flexibility
  **
* Our library was the **first** to be added to the **official** AAIO wiki
* **Modern**, strict code for Python 3.7

## Library Installation

* Install via pip: `pip install aaio`
* Download sources - `git clone https://github.com/kewldan/AAIO`

## Getting Started

### Get user balance

> #### Note that the `AAIO` constructor is called in the async function! [Problem related to calling in sync function](https://stackoverflow.com/questions/52232177/runtimeerror-timeout-context-manager-should-be-used-inside-a-task)

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
  payment_url = client.create_payment(100, 'my_order_id', 'My order description', 'qiwi', 'support@aaio.io',
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

> #### The session is closed automatically when the object is deleted (when `__del__()` is called)

## Contact

E-Mail - kewldanil1@gmail.com
Telegram - [@kewldan](https://t.me/kewldan)

## License

Released under [MIT](/LICENSE) by [@kewldan](https://github.com/kewldan).
