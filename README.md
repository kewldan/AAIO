# AAIO API for Python 3

<a href="https://aaio.io/" target="_blank">
	<img src="https://aaio.io/assets/svg/banners/big/dark-2.svg" title="Aaio - Сервис по приему онлайн платежей">
</a>

[AAIO Official documentation](https://wiki.aaio.io/)

## About

This library is a wrapper for the https://aaio.io API **from enthusiasts**. All methods are described and all types are
explicitly defined. The library does not handle any exceptions, so be careful. Methods that create requests to aaio.io
return an unprocessed server response in JSON format (Parsing JSON on the library side). A new session is used for each request. (Maybe will be
revised in future). Please write about all problems related to the library in issues. API is up-to-date as of *25 August
2023*.

* PyPl - https://pypi.org/project/aaio/
* Github - https://github.com/kewldan/AAIO
* Requirements: Python >= 3.6
* Added to AAIO SDKs

## Library Installation

* Install via pip: `pip install aaio`
* Download sources - `git clone https://github.com/kewldan/AAIO`

## Getting Started

### Get user balance

```python
import asyncio

import aaio


async def main():
    client = aaio.AAIO('MERCHANT ID', 'SECRET KEY', 'API KEY')
    balances = await client.get_balances()
    #  balances = {
    #      "type": "success",
    #      "balance": 50.43, // Текущий доступный баланс
    #      "referal": 0, // Текущий реферальный баланс
    #      "hold": 1.57 // Текущий замороженный баланс
    #  }
    balance = balances['balance']
    print(balance)  # 50.43


asyncio.run(main())
```

### Create payment URL for customer

```python
import aaio

client = aaio.AAIO('MERCHANT ID', 'SECRET KEY', 'API KEY')
payment_url = client.create_payment(100, 'my_order_id', 'My order description', 'qiwi', 'support@aaio.io',
                                    'referral code', currency='USD',
                                    language='en')  # Not send request, just build a URL from parameters!
print(payment_url)  # Prints payment url for customer
```

#### Contact
E-Mail - kewldanil1@gmail.com
Telegram - [@kewldan](https://t.me/kewldan)
