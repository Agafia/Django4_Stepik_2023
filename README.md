# Django4_Stepik_2023
***
### Новая база PostgreSQL 
#### Создайте миграции (если их нет)

``` python manage.py makemigrations ```

#### Примените миграции к PostgreSQL
``` python manage.py migrate ```

#### Создайте суперпользователя
``` python manage.py createsuperuser ```

***
#### Запуск с docker-compose
``` docker-compose up -d ```

#### Остановка
``` docker-compose down ```

#### Просмотр логов
``` docker-compose logs -f ```

#### Остановка и удаление volumes (очистка данных)**
``` docker-compose down -v ```

#### Проверить переменные
``` docker-compose config ```

