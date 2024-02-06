# Создание заявки

Для создания заявки на вывод нужно вызвать метод

<pre class="language-python"><code class="lang-python"><strong>payoff_id = str(uuid.uuid4())
</strong><strong># Обязательно сохраняйте payoff_id в БД
</strong><strong>await client.create_payoff(method, amount, wallet, payoff_id)
</strong></code></pre>

Для остальных параметров запроса прошу смотреть официальную документацию AAIO по ссылке [https://wiki.aaio.so/api/vyvod-sredstv](https://wiki.aaio.so/api/vyvod-sredstv)
