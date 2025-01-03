# Generated by Django 4.2.7 on 2024-12-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_brand_full_description_category_full_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='custom_description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Кастомное описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='custom_description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Кастомное описание'),
        ),
        migrations.AddField(
            model_name='offer',
            name='custom_description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Кастомное описание'),
        ),
    ]
