# Хорошие практики

### Генерация ID заказа

Очень важно генерировать ID заказа случайно, не привязывать его к данным пользователя. Для этого можно использовать UUID

<pre class="language-python" data-title="На практике" data-line-numbers data-full-width="false"><code class="lang-python"><strong>order_id = str(uuid.uuid4())
</strong><strong># Здесь должна быть запись заказа в БД, где можно указать и идентификатор пользователя
</strong>payment_url: str = client.create_payment(299, order_id) # Заметьте, что метод не асинхронный!
</code></pre>

### Сокращение ссылок для оплаты

Дело в том, что создавая ссылки, создаваемые `create_payment` очень длинные и, например, в телеграмме, при переходе по кнопке с ссылкой выскакивает гигантское сообщение с этой ссылкой, что, честно говоря, выглядит не очень классно. Этого можно избежать использую функцию `aaio.create_invoice`, которая асинхронна, так как отправляет GET запрос по payment\_url. То есть она не заменяет create\_payment, она его дополняет

{% code title="На практике" %}
```python
invoice_url: str = await aaio.create_invoice(payment_url)
```
{% endcode %}
