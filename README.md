# Выполненное тестовое задание для ООО «Митра»

## Для запуска необходимо:

### Настроить виртуальное окружения и установить зависимости
```
> python -m venv venv

> venv\Scripts\activate.bat - для Windows

> source venv/bin/activate - для Linux и MacOS

> python -m pip install -r requirements.txt
```

### Применить миграции
```
> cd src
> python manage.py migrate
```

### Загрузить фикстуру
```
> python manage.py laoddata data.json
```

### Запустить сервер
```
> python manage.py runserver
```