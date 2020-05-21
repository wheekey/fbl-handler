# fbl-handler
Обработчик Feedback loop.

//TODO
- Вопрос: понять, как обновлять данные по подписчику в бд emark.
    Что нужно:
    - Доступ к бд пдлх emark
    - Доступ к бд tgs
  Ответ: 
    ```UPDATE email_list_subscribers 
       SET unsubscribed = UNIX_TIMESTAMP(now()), unsubscribeconfirmed=1 
       WHERE emailaddress = 'dddd@m.ru'``` 

- ~~понять, как извлечь message ID yandex fbl~~ 
- ~~получить список файлов в директории по ssh~~
- Вопрос: понять, как распарсить mail.ru

## Docker
https://hub.docker.com/_/python/
### You can then build and run the Docker image:
```
$ docker build -t fbl-handler .
$ docker run -it --rm fbl-handler
```
### Run script from docker
```
docker run -it -w /usr/src/app -v $(pwd):/usr/src/app fbl-handler bash

docker run -it -v "$(pwd)/:/app/target_dir" fbl-handler bash

// С обновлением директории
docker run -it --mount "type=bind,source=$(pwd),target=/app" fbl-handler bash
```

For many simple, single file projects, you may find it inconvenient to write a complete Dockerfile. 
In such cases, you can run a Python script by using the Python Docker image directly:

```
docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python your-daemon-or-script.py
```

https://docs.djangoproject.com/en/3.0/intro/tutorial01/
https://docs.djangoproject.com/en/3.0/intro/tutorial02/
## Создаем структуру 
```
python manage.py migrate
python manage.py makemigrations fbl_handler
python manage.py sqlmigrate fbl_handler 0001
python manage.py migrate
```

## Tests
```
https://docs.djangoproject.com/en/3.0/intro/tutorial05/
```

