import hashlib

import aiohttp

from .models import PayoffWebhookData


async def create_invoice(payment_url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(payment_url) as request:
            return request.url


def is_valid_payoff_webhook(data: PayoffWebhookData, secret_key: str) -> bool:
    return hashlib.sha256(
        f'{data.id}:{secret_key}:{data.amount_down}'.encode()).hexdigest() == data.sign
