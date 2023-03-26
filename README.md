# pogoda

## Первональные настройки

- Задаем значения для переменных окружения `.env`

- Подставляем название города в файле `config.py`

- Заменяем префикс базы данных wordpress в файлах с sql-запросами
`db_create_tables.sql`, `db_drop_tables.sql`, `db_insert_pogoda_additional.sql`, `db_insert_pogoda_detailed.sql`

- Заменяем префикс в файле плагина `weather-by-month-template.php` 

## Подготовка данных вручную

Копируем содержимое веб страниц из списка в файле url.txt

```cd data/```

Подставляем название города в файле `url.txt`

Сохраняем вебстраницы локально с использованием команды wget

```wget -k -p -E --header='Accept: text/html' --user-agent='Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0' --input-file='url.txt'```

Или сохраняем вебстраницы локально автоматически с cron и wget

```
# Go to vi/pogoda/data/ and start wget
0 1 * * * cd /home/www/vi/pogoda/data/ && wget -k -p -E --header='Accept: text/html' --user-agent='Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0' --input-file='url.txt'
```

