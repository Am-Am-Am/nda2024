# Generated by Django 4.2.7 on 2025-01-19 13:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_alter_offer_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='custom_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='custom_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='db_id',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='custom_description',
        ),
        migrations.AddField(
            model_name='category',
            name='characteristics',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True, verbose_name='Характеристики'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название категории | Заголовок'),
        ),
    ]