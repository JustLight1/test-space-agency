<a id="anchor"></a>
<div align=center>

  # Тестовое задание

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

</div>

## Описание тестового задания

```
- Сборку проекта осуществить с помощью python 3.9, Django 4.1 и MySQL;
- Для сборки клиентской части страницы необходимо использовать bootstrap 5;
- Для запуска слайдера необходимо использовать slick slider http://kenwheeler.github.io/slick/ (см. Slider Syncing);
- По клику на большую фотографию на слайдере фотки должны открываться на весь экран и листаться галереей;
- Необходимо чтобы slider заполнялся через админку django. Необходимо настроить визуально понятный admin.py, чтобы выводилась картинка и название в списке записей элементов слайдера;
- Для картинок модели слайдера необходимо использовать пакет django-filer и через него грузить картинки в слайдер;
- Записи слайдера в админке должны сортироваться при помощи drag&drop, для этого необходимо использовать пакет django-admin-sortable2;
```

### Технологии

Python 3.9.10

Django 4.2

Django-admin-sortable2

Django-filer 3

MYSQL

<details>
<summary>
<h4>Запуск проекта</h4>
</summary>

<br>

~~~
склонировать проект git clone git@github.com:JustLight1/test-space-agency.git
~~~
- При первом запуске для функционирования проекта обязательно установить виртуальное окружение, установить зависимости,  выполнить миграции:

```
python -m venv venv

source venv/Scripts/activate

python -m pip install --upgrade pip
```
- Установите зависимости из файла requirements.txt

```
pip install -r requirements.txt
```
- Выполните миграции БД. Из папки backend с файлом manage.py выполните команду:
```
python manage.py makemigrations
python manage.py migrate
```
- Для создания суперюзера из папки backend с файлом manage.py выполните команду:
```
python manage.py createsuperuser
```

- Для запуска сервера из папки backend с файлом manage.py выполните команду:

```
python manage.py runserver
```
</details>


<details>
<summary>
<h4>Шаблон наполнения env-файла</h4>
</summary>

- Для работы с MYSQL необходимо установить DEBUG=False или True для работы с SQLite

<br>

```env
  DEBUG=False

  MYSQL_DATABASE=...
  MYSQL_USER=...
  MYSQL_PASSWORD=...
  MYSQL_ROOT_PASSWORD=...


  DB_HOST=...
  DB_PORT=...
```

</details>

## Контакты:

**Форов Александр** 

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)
