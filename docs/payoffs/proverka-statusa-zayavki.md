# Проверка статуса заявки

Для проверки статуса заявки необходимо вызвать метод и проверить поле `status`

```python
info = await client.get_payoff_info(payoff_id)

print(info.status) # in_process, cancel, success
```

Для остальных параметров запроса прошу смотреть официальную документацию AAIO по ссылке [https://wiki.aaio.so/api/informaciya-o-zayavke-na-vyvod-sredstv](https://wiki.aaio.so/api/informaciya-o-zayavke-na-vyvod-sredstv)
