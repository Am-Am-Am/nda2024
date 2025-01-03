# Generated by Django 4.2.7 on 2024-12-19 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_category_ru'),
        ('files', '0003_delete_modelfilevideo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelfile',
            options={'verbose_name_plural': 'РУ и Сертификаты'},
        ),
        migrations.CreateModel(
            name='InstructionsFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='category/instructions')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category')),
            ],
            options={
                'verbose_name_plural': 'Инструкции',
            },
        ),
        migrations.CreateModel(
            name='CatalogFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='category/catalog')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category')),
            ],
            options={
                'verbose_name_plural': 'Каталог',
            },
        ),
    ]
