# Generated by Django 4.2.7 on 2024-12-11 09:00

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_offer_shipping_pack_alter_brand_banner_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='instruction',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/files', location='C:\\Users\\amur_\\Downloads\\nda2024-1\\privateprivate/'), upload_to='instructions', verbose_name='Инструкция'),
        ),
    ]
