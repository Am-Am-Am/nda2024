# Generated by Django 4.2.7 on 2025-01-19 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_delete_product_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offer', to='catalog.product', verbose_name='Категория, к которой принадлежит товар'),
        ),
    ]