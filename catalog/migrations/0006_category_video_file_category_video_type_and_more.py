# Generated by Django 4.2.7 on 2024-12-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_category_instruction'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='category/videos', verbose_name='Загрузите видеофайл'),
        ),
        migrations.AddField(
            model_name='category',
            name='video_type',
            field=models.CharField(choices=[('simple', 'Просто видео'), ('youtube', 'Видео с YouTube'), ('vk', 'Видео с ВКонтакте')], default='simple', max_length=10, verbose_name='Тип видео'),
        ),
        migrations.AddField(
            model_name='category',
            name='vk_url',
            field=models.URLField(blank=True, max_length=256, null=True, verbose_name='Ссылка на видео ВКонтакте'),
        ),
        migrations.AddField(
            model_name='category',
            name='youtube_url',
            field=models.URLField(blank=True, max_length=256, null=True, verbose_name='Ссылка на видео YouTube'),
        ),
    ]
