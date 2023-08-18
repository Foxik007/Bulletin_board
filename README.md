# Bulletin_board
Доска обьявлений по типу Авито<br>
<h2><b>Сайт написан на Django</h2></b>

![247908741-131edf40-b666-4e22-87aa-1caf407a3091](https://github.com/Foxik007/Bulletin_board/assets/85826675/a9d6c6fd-1cb8-43cd-ade4-ed037b5c8cbe)

Устанавливаем все пакеты <br>
```pip install -r requirements.txt```

Выполняем команды:<br>
```
python manage.py makemigrations
python manage.py migrate
```

Создаем администратора
```
python manage.py createsuperuser
```

Собираем статические файлы
```
python manage.py collectstatic
```

Запускаем проект

```
python manage.py runserver
```
