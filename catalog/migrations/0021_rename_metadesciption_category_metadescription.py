# Generated by Django 4.2.7 on 2024-12-24 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_category_metadesciption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='metadesciption',
            new_name='metadescription',
        ),
    ]
