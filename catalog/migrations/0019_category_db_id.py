# Generated by Django 4.2.7 on 2024-12-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_brand_custom_description_category_custom_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='db_id',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Id со старой бд'),
        ),
    ]