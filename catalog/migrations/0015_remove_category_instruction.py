# Generated by Django 4.2.7 on 2024-12-19 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_category_ru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='instruction',
        ),
    ]
