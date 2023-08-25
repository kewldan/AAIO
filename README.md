# AAIO API for Python 3

<a href="https://aaio.io/" target="_blank">
	<img src="https://aaio.io/assets/svg/banners/big/dark-2.svg" title="Aaio - Сервис по приему онлайн платежей">
</a>

[AAIO Official documentation](https://wiki.aaio.io/)

### About

This library is a wrapper for the https://aaio.io API **from enthusiasts**. All methods are described and all types are
explicitly defined. The library does not handle any exceptions, so be careful. Methods that create requests to aaio.io
return an unprocessed server response in JSON format (Parsing JSON on the library side). But the `create_payment()`
method for example
returns a reference (str) and does not create any I/O bound load. A new session is used for each request. (Maybe will be
revised in future). Please write about all problems related to the library in issues. API is up-to-date as of *25 August
2023*.

### Download

* `pip install aaio`
* Website - [PyPi](https://pypi.org/project/aaio/)
* Github - [github](https://github.com/kewldan/AAIO)
* Sources - `git clone https://github.com/kewldan/AAIO`

### Dependencies

* aiohttp - `pip install aiohttp` [Official website](https://docs.aiohttp.org/en/stable/)

### Usage

1. Get on-hold balance of user

```python
import asyncio

import aaio


async def main():
    client = aaio.AAIO('MERCHANT ID', 'SECRET KEY', 'API KEY')
    balances = await client.get_balances()  # {'balance': 100, 'hold': }
    on_hold = balances['hold']
    print(on_hold)


asyncio.run(main())
```