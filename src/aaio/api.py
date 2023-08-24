import hashlib
from urllib.parse import urlencode

import aiohttp

from aaio.exceptions import RequestErrorException

aaio_payoff_methods = [
    {'name': 'QIWI', 'code': 'qiwi'},
    {'name': 'Yoomoney', 'code': 'yoomoney'},
    {'name': 'Payeer', 'code': 'payeer'},
    {'name': 'Карта 🇷🇺', 'code': 'cards_ru'},
    {'name': 'Perfect money', 'code': 'perfectmoney'},
    {'name': 'Карта 🇺🇦', 'code': 'cards_ua'},
    {'name': 'Карта СНГ', 'code': 'cards_sng'},
    {'name': 'Tether', 'code': 'tether_trc20'},
    {'name': 'Bitcoin', 'code': 'bitcoin'},
]


def get_method_name_by_code(code: str):
    for method in aaio_payoff_methods:
        if method['code'] == code:
            return method['name']


class AAIO:
    def __init__(self, merchant_id: str, secret: str, api_key: str, default_currency: str = 'RUB',
                 base_url: str = 'https://aaio.io'):
        self.default_currency = default_currency
        self.merchant_id = merchant_id
        self.api_key = api_key
        self.secret = secret
        self.base_url = base_url

    def __generate_sign(self, amount: float, order_id: str, currency: str) -> str:
        params = f':'.join([
            self.merchant_id,
            str(amount),
            currency,
            self.secret,
            order_id
        ])
        sign = hashlib.sha256(params.encode('utf-8')).hexdigest()
        return sign

    def create_payment(self, amount: float, description: str, order_id: str, method: str = None, email: str = None,
                       referral: str = None, us_key: str = None, currency: str = None,
                       language: str = 'ru') -> str:
        if not currency:
            currency = self.default_currency
        params = {
            'merchant_id': self.merchant_id,
            'amount': amount,
            'currency': currency,
            'order_id': order_id,
            'sign': self.__generate_sign(amount, order_id, currency),
            'desc': description,
            'lang': language,
            'method': method,
            'email': email,
            'referal': referral,
            'us_key': us_key
        }
        return f'{self.base_url}/merchant/pay?' + urlencode(params)

    async def get_pay_info(self, order_id: str):
        params = {
            'merchant_id': self.merchant_id,
            'order_id': order_id
        }

        return await self.__create_request('/api/info-pay', params)

    async def get_balances(self):
        return await self.__create_request('/api/balance')

    async def create_payoff(self, method: str, amount: float, wallet: str, payoff_id: str = '',
                            commission_type: int = 0):
        params = {
            'my_id': payoff_id,
            'method': method,
            'amount': amount,
            'wallet': wallet,
            'commission_type': commission_type
        }
        return await self.__create_request('/api/create-payoff', params)

    async def info_payoff(self, payoff_id: str = None, aaio_id: str = None):
        params = {
            'my_id': payoff_id,
            'id': aaio_id
        }
        return await self.__create_request('/api/info-payoff', params)

    async def rates_payoff(self):
        return await self.__create_request('/api/rates-payoff')

    async def methods_payoff(self):
        return await self.__create_request('/api/methods-payoff')

    async def methods_pay(self):
        params = {
            'merchant_id': self.merchant_id
        }
        return await self.__create_request('/api/methods-pay', params)

    async def __create_request(self, uri: str, params: dict = None):
        if params is None:
            params = {}
        headers = {
            'Accept': 'application/json',
            'X-Api-Key': self.api_key
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.base_url}{uri}', headers=headers, data=params) as r:
                response = await r.json()
                if 'type' in response:
                    return response
                raise RequestErrorException(f'AAIO returned invalid response ({self.base_url}{uri}): {response}')
