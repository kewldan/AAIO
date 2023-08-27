# AAIO API for Python 3

<a href="https://aaio.io/" target="_blank">
	<img src="https://aaio.io/assets/svg/banners/big/dark-2.svg" title="Aaio - Сервис по приему онлайн платежей">
</a>

[AAIO Official documentation](https://wiki.aaio.io/)

## About

**Currently, when trying to get the exchange rate, a 404 error is generated due to issues on the AAIO side. A fix is expected on 28 August**

This library is a wrapper for the https://aaio.io API **from enthusiasts**. All methods are described and all types are
**explicitly** defined. The library does **not handle any exceptions**, so be careful. Methods that create requests to aaio.io
return an **unprocessed server response** in JSON format (Parsing JSON on the library side). Please write about all problems related to the library to [issues](https://github.com/kewldan/AAIO/issues). API is up-to-date as of *28 August
2023*.

Latest major changes (v1.0.6): A session is now **not created** on every request. (This can **speed things up** considerably follow the aiohttp documentation) In case of any problems with this please open issues and temporarily roll back to version 1.0.5

* PyPl - https://pypi.org/project/aaio/
* Github - https://github.com/kewldan/AAIO
* Requirements: Python >= 3.6
* Added to [AAIO SDKs](https://wiki.aaio.io/priem-platezhei/gotovye-cms-moduli-i-sdk/python-3-sdk)

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

### Create payoff

```python
import asyncio

import aaio


async def main():
    client = aaio.AAIO('MERCHANT ID', 'SECRET KEY', 'API KEY')
    payoff = await client.create_payoff('qiwi', 100.35, '79998887766', 'my_payoff_id')
    # {
	#     "type": "success",
	#     "id": "52a16aea-d308-11ed-afa1-0242ac120002", // ID Вывода средств в нашей системе
	#     "my_id": "my_id_123", // ID Вывода средств в Вашей системе
	#     "method": "tether_trc20", // Кодовое название платежной системы
	#     "wallet": "*********", // Номер счета/кошелька
	#     "amount": 485, // Придёт на счет (в RUB)
	#     "amount_in_currency": 5, // Придёт на счет (в валюте)
	#     "amount_currency": "USDT", // Валюта отправки на счет
	#     "amount_rate": 96.92, // Курс конвертации
	#     "amount_down": 500, // Списано с баланса (в RUB)
	#     "commission": 15, // Сумма комисии (в RUB)
	#     "commission_type": 0, // Тип комиссии
	#     "status": "in_process" // Статус (in_process - в процессе, cancel - отменено, success - выполнено)
    # }
    print(payoff['status'])  # in_progress


asyncio.run(main())
```

## Contact
E-Mail - kewldanil1@gmail.com
Telegram - [@kewldan](https://t.me/kewldan)
