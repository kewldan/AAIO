import hashlib
from typing import Optional, List
from urllib.parse import urlencode

import aiohttp

from aaio.exceptions.aaio_bad_request import AAIOBadRequest
from aaio.types.balance import Balance
from aaio.types.create_payoff import CreatePayoff
from aaio.types.payment_info import PaymentInfo
from aaio.types.payment_methods import PaymentMethods
from aaio.types.payoff_info import PayoffInfo
from aaio.types.payoff_methods import PayoffMethods
from aaio.types.payoff_rates import PayoffRates
from aaio.types.payoff_sbp_banks import PayoffSbpBanks


async def create_invoice(payment_url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(payment_url) as request:
            return request.url


class AAIO:
    """
    AAIO client for API interaction
    Session will be automatically closed

    API for https://aaio.so/
    """

    def __init__(self, merchant_id: str, secret: str, api_key: str, default_currency: str = 'RUB',
                 base_url: str = 'https://aaio.so'):
        """
        Creates instance of one AAIO merchant API client

        Args:
            merchant_id: Merchant ID from https://aaio.so/cabinet
            secret: 1st secret key from https://aaio.so/cabinet
            api_key: API key from https://aaio.so/cabinet/api
            default_currency: If not set - RUB, but can be overwritten for each request (Optional)
            base_url: Base URL for requests (Optional)
        """

        self._default_currency = default_currency
        self._merchant_id = merchant_id
        self._api_key = api_key
        self._secret = secret
        self._base_url = base_url

    def __generate_sign(self, amount: float, order_id: str, currency: str) -> str:
        """
        Generates sign for payment creation
        See https://wiki.aaio.so/priem-platezhei/sozdanie-zakaza/metodika-formirovaniya-podpisi

        Args:
            amount: Amount in your currency
            order_id: Your order ID
            currency: Currency

        Returns: SHA-256 sign

        """

        params = f':'.join([
            self._merchant_id,
            str(amount),
            currency,
            self._secret,
            order_id
        ])
        sign = hashlib.sha256(params.encode('utf-8')).hexdigest()
        return sign

    def create_payment(self, amount: float, order_id: str, description: str = None, method: str = None,
                       email: str = None,
                       referral: str = None, us_key: str = None, currency: str = None,
                       language: str = 'ru') -> str:
        """
        Creates payment URL (Not a request)
        See https://wiki.aaio.so/priem-platezhei/sozdanie-zakaza for more detailed information

        Args:
            amount: Payment amount
            order_id: Your order id
            description: Payment description (Optional)
            method: Payment method, can be overwritten by customer (Optional)
            email: Client E-Mail (Optional)
            referral: Referral code for cookies (Optional)
            us_key: Custom parameters (Optional)
            currency: Payment currency, default - default client currency (Optional)
            language: Page language (Optional)

        Returns: Payment URL

        """

        if not currency:
            currency = self._default_currency
        params = {
            'merchant_id': self._merchant_id,
            'amount': amount,
            'currency': currency,
            'order_id': order_id,
            'sign': self.__generate_sign(amount, order_id, currency),
            'desc': description,
            'lang': language,
            'method': method,
            'email': email,
            'referral': referral,
            'us_key': us_key
        }

        return f'{self._base_url}/merchant/pay?' + urlencode({k: v for k, v in params.items() if v is not None})

    async def get_ips(self) -> List[str]:
        response = await self.__create_request('/api/public/ips')

        return response['list']

    async def get_payment_info(self, order_id: str) -> PaymentInfo:
        """
        Creates a request for get payment information
        See https://wiki.aaio.so/api/informaciya-o-zakaze

        Args:
            order_id: Your order ID

        Returns: Model from response JSON

        """

        params = {
            'merchant_id': self._merchant_id,
            'order_id': order_id
        }

        response = await self.__create_request('/api/info-pay', params)

        return PaymentInfo(**response)

    async def get_balances(self) -> Balance:
        """
        Creates a request for get balances of user
        See https://wiki.aaio.so/api/poluchenie-balansa

        Returns: Model from response JSON
        """

        response = await self.__create_request('/api/balance')

        return Balance(**response)

    async def create_payoff(self, method: str, amount: float, wallet: str, payoff_id: str = '',
                            commission_type: int = 0) -> CreatePayoff:
        """
        Creates a request for payoff creating
        See https://wiki.aaio.so/api/vyvod-sredstv

        Args:
            method: Payoff method
            amount: Payoff amount
            wallet: Payoff wallet
            payoff_id: Your payoff ID (Optional)
            commission_type: Commission type, default - 0 (Optional)

        Returns: Model from response JSON

        """

        params = {
            'my_id': payoff_id,
            'method': method,
            'amount': amount,
            'wallet': wallet,
            'commission_type': commission_type
        }

        response = await self.__create_request('/api/create-payoff', params)

        return CreatePayoff(**response)

    async def get_payoff_sbp_banks(self) -> PayoffSbpBanks:
        """
        Returns a list of available banks for payoff
        See https://wiki.aaio.so/api/banki-dlya-vyvoda-sredstv-na-sbp
        Returns: list of banks
        """
        response = await self.__create_request('/api/sbp-banks-payoff')

        return PayoffSbpBanks(**response)

    async def get_payoff_info(self, payoff_id: str = None, aaio_id: str = None) -> PayoffInfo:
        """
        Creates a request for get payoff information
        See https://wiki.aaio.so/api/informaciya-o-zayavke-na-vyvod-sredstv

        One id is required!

        Args:
            payoff_id: Your payoff ID (Optional)
            aaio_id: AAIO payoff ID (Optional)

        Returns: Model from response JSON

        """

        params = {
            'my_id': payoff_id,
            'id': aaio_id
        }

        response = await self.__create_request('/api/info-payoff', params)

        return PayoffInfo(**response)

    async def get_payoff_rates(self) -> PayoffRates:
        """
        Creates a request for get rates for payoff
        See https://wiki.aaio.so/api/kurs-valyut-pri-vyvode-sredstv

        Returns: Model from response JSON

        """

        response = await self.__create_request('/api/rates-payoff')

        return PayoffRates(**response)

    async def get_payoff_methods(self) -> PayoffMethods:
        """
        Creates a request for get available payoff methods
        See https://wiki.aaio.so/api/dostupnye-metody-dlya-vyvoda-sredstv

        Returns: Model from response JSON

        """

        response = await self.__create_request('/api/methods-payoff')

        return PayoffMethods(**response)

    async def get_payment_methods(self) -> PaymentMethods:
        """
        Creates a request for get available payment methods
        See https://wiki.aaio.so/api/dostupnye-metody-dlya-sozdaniya-zakaza

        Returns: Model from response JSON

        """

        params = {
            'merchant_id': self._merchant_id
        }

        response = await self.__create_request('/api/methods-pay', params)

        return PaymentMethods(**response)

    async def __create_request(self, uri: str, params: dict = None) -> Optional[dict]:
        """
        Creates a request to base URL and adds URI

        Args:
            uri: URI
            params: Request params (Optional)

        Returns: Model from response JSON

        """

        if params is None:
            params = {}

        headers = {
            'Accept': 'application/json',
            'X-Api-Key': self._api_key
        }

        async with aiohttp.ClientSession(self._base_url) as session:
            async with session.post(uri, headers=headers,
                                    data={k: v for k, v in params.items() if v is not None}) as r:
                response = await r.json(content_type=None)
                if response['type'] == 'success':
                    return response
                else:
                    raise AAIOBadRequest(response['code'], response['message'])
