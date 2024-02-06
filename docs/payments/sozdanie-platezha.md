# Создание платежа

Для создания заявки нужно просто сгенерировать URL для отправки пользователю

```python
payment_url: str = client.create_payment(amount, order_id)
```

Прошу сразу посетить [khoroshie-praktiki.md](../khoroshie-praktiki.md "mention") для полезной информации

Для остальных параметров запроса прошу смотреть оффициальную документацию AAIO по ссылке [https://wiki.aaio.so/priem-platezhei/sozdanie-zakaza](https://wiki.aaio.so/priem-platezhei/sozdanie-zakaza)
