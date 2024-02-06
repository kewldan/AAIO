# Проверка статуса платежа

Для проверки статуса платежа необходимо вызвать метод

```python
info = await client.get_payment_info(order_id)

print(info) # in_process, success, hold, expired
```

Для остальных параметров запроса прошу смотреть оффициальную документацию AAIO по ссылке [https://wiki.aaio.so/api/informaciya-o-zakaze](https://wiki.aaio.so/api/informaciya-o-zakaze)
