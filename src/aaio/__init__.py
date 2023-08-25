class AAIO:
    """
    AAIO client for API interaction

    API for https://aaio.io/
    """

    def __init__(self, merchant_id: str, secret: str, api_key: str, default_currency: str = 'RUB',
                 base_url: str = 'https://aaio.io'):
        """
        Creates instance of one AAIO merchant API client

        Args:
            merchant_id: Merchant ID from https://aaio.io/cabinet
            secret: 1st secret key from https://aaio.io/cabinet
            api_key: API key from https://aaio.io/cabinet/api
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
        See https://wiki.aaio.io/priem-platezhei/sozdanie-zakaza/metodika-formirovaniya-podpisi

        Args:
            amount: Amount in your currency
            order_id: Your order ID
            currency: Currency

        Returns:SHA-256 sign

        """

        import hashlib

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
        See https://wiki.aaio.io/priem-platezhei/sozdanie-zakaza for more detailed information

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
        from urllib.parse import urlencode

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
            'referal': referral,
            'us_key': us_key
        }
        return f'{self._base_url}/merchant/pay?' + urlencode(params)

    async def get_pay_info(self, order_id: str) -> dict:
        """
        Creates a request for get payment information
        See https://wiki.aaio.io/api/informaciya-o-zakaze

        Args:
            order_id: Your order ID

        Returns: Response JSON

        """

        params = {
            'merchant_id': self._merchant_id,
            'order_id': order_id
        }

        return await self.__create_request('/api/info-pay', params)

    async def get_balances(self) -> dict:
        """
        Creates a request for get balances of user
        See https://wiki.aaio.io/api/poluchenie-balansa

        Returns: Response JSON
        """

        return await self.__create_request('/api/balance')

    async def create_payoff(self, method: str, amount: float, wallet: str, payoff_id: str = '',
                            commission_type: int = 0) -> dict:
        """
        Creates a request for payoff creating
        See https://wiki.aaio.io/api/vyvod-sredstv

        Args:
            method: Payoff method
            amount: Payoff amount
            wallet: Payoff wallet
            payoff_id: Your payoff ID (Optional)
            commission_type: Commission type, default - 0 (Optional)

        Returns: Response JSON

        """

        params = {
            'my_id': payoff_id,
            'method': method,
            'amount': amount,
            'wallet': wallet,
            'commission_type': commission_type
        }
        return await self.__create_request('/api/create-payoff', params)

    async def info_payoff(self, payoff_id: str = None, aaio_id: str = None) -> dict:
        """
        Creates a request for get payoff information
        See https://wiki.aaio.io/api/informaciya-o-zayavke-na-vyvod-sredstv

        One id is required!

        Args:
            payoff_id: Your payoff ID (Optional)
            aaio_id: AAIO payoff ID (Optional)

        Returns: Response JSON

        """

        params = {
            'my_id': payoff_id,
            'id': aaio_id
        }
        return await self.__create_request('/api/info-payoff', params)

    async def rates_payoff(self) -> dict:
        """
        Creates a request for get rates for payoff
        See https://wiki.aaio.io/api/kurs-valyut-pri-vyvode-sredstv

        Returns: Response JSON

        """

        return await self.__create_request('/api/rates-payoff')

    async def methods_payoff(self) -> dict:
        """
        Creates a request for get available payoff methods
        See https://wiki.aaio.io/api/dostupnye-metody-dlya-vyvoda-sredstv

        Returns: Response JSON

        """

        return await self.__create_request('/api/methods-payoff')

    async def methods_pay(self) -> dict:
        """
        Creates a request for get available payment methods
        See https://wiki.aaio.io/api/dostupnye-metody-dlya-sozdaniya-zakaza

        Returns: Response JSON

        """

        params = {
            'merchant_id': self._merchant_id
        }
        return await self.__create_request('/api/methods-pay', params)

    async def __create_request(self, uri: str, params: dict = None):
        """
        Creates a request to base URL and adds URI

        Args:
            uri: URI
            params: Request params (Optional)

        Returns: Response JSON

        """

        import aiohttp

        if params is None:
            params = {}
        headers = {
            'Accept': 'application/json',
            'X-Api-Key': self._api_key
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self._base_url}{uri}', headers=headers, data=params) as r:
                return await r.json()
