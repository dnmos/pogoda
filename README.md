# pogoda

## Подготовка данных вручную
Копируем содержимое веб страниц из списку в файле url.txt

```cd data/```

```wget -k -p -E --header='Accept: text/html' --user-agent='Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0' --input-file='url.txt'
```

## Подготовка данных с помощью cron

```0,30 * * * * /usr/bin/wget  -k -p -E --header='Accept: text/html' --user-agent='Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0' --input-file='url.txt' /pogoda/my_result.file --no-check-certificate```