import mysql.connector
import os
import sys
from django.conf import settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(BASE_DIR, '..')
sys.path.append(PROJECT_ROOT)

# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nda.settings") 

import django
django.setup()

from catalog.models import (
    Category,
    Brand,
    Offer,
)  # Replace "catalog" with app name
from django.utils.text import slugify

sql_host = settings.SQL_HOST
sql_user = settings.SQL_USER
sql_password = settings.SQL_PASSWORD
sql_base_name = settings.SQL_BASE_NAME
# Данные для подключения к базе данных
config = {
    "host": sql_host,  # IP-адрес или доменное имя сервера MySQL
    "user": sql_user,  # Имя пользователя MySQL
    "password": sql_password,  # Пароль пользователя MySQL
    "database": sql_base_name,  # Название базы данных
}


# Устанавливаем соединение с базой данных
connection = mysql.connector.connect(**config)


def create_brand(name, slug):
    simple_brand = Brand.objects.create(
        name = name,
        slug = slug,
    )
    print(f"Создан бренд: {simple_brand}")

create_brand('Общий бренд', 'brand_from_db')

def create_category(id, name, slug, image, description, custom_description, ordering, brand="Общий бренд"):

    slug = slugify(slug)

    # Проверяем существование slug и генерируем новый, если необходимо
    original_slug = slug
    if Category.objects.filter(slug=slug).exists():
        count = 1
        new_slug = f"{slug}-{count}"
        while Category.objects.filter(slug=new_slug).exists():
            count += 1
            new_slug = f"{slug}-{count}"
        slug = new_slug  # Присваиваем новый slug

    try:
        brand_obj = Brand.objects.get(name=brand)
    except Brand.DoesNotExist:
        brand_obj = None

    simple_cat = Category.objects.create(
        db_id = id,
        brand=brand_obj,
        name=name,
        logo=image,
        slug=slug,
        description=description,
        custom_description=custom_description,
        place=ordering,
        is_final=False,
        # Другие поля будут использовать значения по умолчанию или допускать NULL
    )
    print(f"Создана категория: {simple_cat} с slug: {slug}")



def get_categories_from_sql():
    with connection.cursor() as cursor:

        cursor.execute("SELECT id FROM jmTw_k2_categories")
        ids = cursor.fetchall()

        cursor.execute("SELECT name FROM jmTw_k2_categories")
        names = cursor.fetchall()

        cursor.execute("SELECT alias FROM jmTw_k2_categories")
        slugs = cursor.fetchall()

        cursor.execute("SELECT image FROM jmTw_k2_categories")
        images = cursor.fetchall()

        cursor.execute("SELECT description FROM jmTw_k2_categories")
        descriptions = cursor.fetchall()

        cursor.execute("SELECT customdesc FROM jmTw_k2_categories")
        custom_descriptions = cursor.fetchall()

        cursor.execute("SELECT ordering FROM jmTw_k2_categories")
        orderings = cursor.fetchall()




    results_object = {
        "names": names,
        "slugs": slugs,
        "images": images,
        "descriptions": descriptions,
        "custom_descriptions":custom_descriptions,
        "ids":ids,
        "orderings":orderings
    }

    return results_object


resultsCategories = get_categories_from_sql()

names = resultsCategories["names"]
slugs = resultsCategories["slugs"]
images = resultsCategories["images"]
descriptions = resultsCategories["descriptions"]
custom_descriptions = resultsCategories["custom_descriptions"]
ids = resultsCategories['ids']
orderings = resultsCategories['orderings']

# Ensure the lists have the same length
if len(names) != len(slugs):
    print("Error: Name and slug lists have different lengths.")
else:
    # Loop through the lists, pairing names and slugs by index
    for index in range(len(names)):
        ids_tuple = ids[index]
        name_tuple = names[index]  
        slug_tuple = slugs[index]  
        image_tuple = images[index]
        descriptions_tuple = descriptions[index]
        custom_descriptions_tuple = custom_descriptions[index]
        orderings_tuple = orderings[index]

        id = ids_tuple[0]
        name = name_tuple[0] 
        slug = slug_tuple[0] 
        image = image_tuple[0]
        description = descriptions_tuple[0]
        custom_description = custom_descriptions_tuple[0]
        ordering = orderings_tuple[0]

        create_category(id, name, slug, image, description, custom_description, ordering)
        # print(id, name, slug, image, description, custom_description, ordering)


def create_item(id, name, cat_id):
    try:
        category_obj = Category.objects.get(db_id=cat_id)
    except Category.DoesNotExist:
        category_obj = None

    simple_item = Offer.objects.create(
        category=category_obj,
        name=name,
        # Другие поля будут использовать значения по умолчанию или допускать NULL
    )
    print(f"Создан товар: {simple_item} с slug: {slug}")



def get_items_from_sql():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM jmtw_k2_items")
        ids = cursor.fetchall()

        cursor.execute("SELECT title FROM jmtw_k2_items")
        names = cursor.fetchall()

        cursor.execute("SELECT catid FROM jmtw_k2_items")
        cat_ids = cursor.fetchall()

        results_object = {
        "names": names,
        "cat_ids": cat_ids,
        "ids":ids,
    }

    return results_object


resultsItems = get_items_from_sql()

names = resultsItems["names"]
cat_ids = resultsItems['cat_ids']
ids = resultsItems['ids']


for index in range(len(names)):
    ids_tuple = ids[index]
    name_tuple = names[index]  
    cat_ids_tuple = cat_ids[index]

    id = ids_tuple[0]
    cat_id = cat_ids_tuple[0]
    name = name_tuple[0] 
    
    print(id, cat_id, name)
    create_item(id, name, cat_id)

    