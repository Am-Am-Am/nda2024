# Generated by Django 4.2.7 on 2024-12-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_mainpageinfoblock_block_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpageinfoblock',
            name='block_text',
            field=models.TextField(blank=True, default='<ul>\n                    <li><span>Особенность 1</span>\xa0</li>\n                    <li><span>Особенность 2</span></li>\n                </ul>', null=True, verbose_name='Описание'),
        ),
    ]