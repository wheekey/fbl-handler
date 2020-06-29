# fbl-handler
Обработчик Feedback loop.


Для pdlx и тогаса скрипт расположен на каждом сервере
# Боевой сервер
/home/admin/projects/fbl-handler





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

#Deployment
```
# Заходим в докер и запускаем миграцию

docker run -v "$(pwd):/usr/src/app" -it fbl-handler bash
python manage.py migrate

```

#Запуск
```
$ docker build -t fbl-handler-pdlx .
$ docker run -it -v "$(pwd):/usr/src/app" fbl-handler
```

# Запуск по крону
```
0 * * * * docker run  -v "/home/admin/projects/fbl-handler:/usr/src/app" fbl-handler > /home/admin/projects/fbl-handler/debug.log 2>&1
0 * * * * docker run  -v "/home/admin/projects/fbl-handler-pdlx:/usr/src/app" fbl-handler-pdlx > /home/admin/projects/fbl-handler-pdlx/debug.log 2>&1
```

### Run script from docker
```
docker run -it -w /usr/src/app -v $(pwd):/usr/src/app fbl-handler bash

docker run -it -v "$(pwd)/:/app/target_dir" fbl-handler bash

// https://stackoverflow.com/questions/47542956/how-to-synchronize-host-folder-in-container-folder-with-docker?answertab=votes#tab-top
docker run -v <host_dir>:<container_dir> -other options imagename

//
docker run -v "$(pwd):/usr/src/app" -it fbl-handler bash

// С обновлением директории
docker run -it --mount "type=bind,source=$(pwd),target=/app" fbl-handler bash
```

For many simple, single file projects, you may find it inconvenient to write a complete Dockerfile. 
In such cases, you can run a Python script by using the Python Docker image directly:

```
docker run -it --rm --name my-running-script -v "$PWD":/usr/src/app -w /usr/src/app python:3 python index.py
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

