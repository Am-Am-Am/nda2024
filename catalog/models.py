from django.db import models
from django.forms import ValidationError
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.core.validators import URLValidator, ValidationError
from django.utils.text import slugify
from nda.settings import PRIVATE_ROOT, SENDFILE_ROOT
from ckeditor.fields import RichTextField

private_storage = FileSystemStorage(location=PRIVATE_ROOT + SENDFILE_ROOT, base_url='/files')


"""Общие классы и миксины"""


class NotHidden(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='PUBLISHED')


class BaseFields(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Черновик'
        PUBLISHED = 'PUBLISHED', 'Активен'
        ARCHIVED = 'ARCHIVED', 'В архиве'

    description = RichTextField(
        default='',
        null=True,
        blank=True,
        verbose_name='Краткое описание',
        config_name='default'  # Используем конфигурацию по умолчанию
    )

    full_description = RichTextField(
        default='',
        null=True,
        blank=True,
        verbose_name='Полное описание',
        config_name='default'
    )
    place = models.IntegerField(
        blank=True,
        null=True,
        default=0,  # Добавлено значение по умолчанию
        verbose_name='Место в списке'
    )
    status = models.CharField(
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='Статус показа на страницах'
    )

    objects = models.Manager()
    visible = NotHidden()

    class Meta:
        abstract = True


"""Модели"""


class Brand(BaseFields):
    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='Бренд')
    logo = models.ImageField(
        upload_to='brand/logo',
        default='',
        blank=True,
        verbose_name='Логотип бренда'
    )
    banner = models.ImageField(
        upload_to='brand/banner',
        default='',
        blank=True,
        verbose_name='Баннер бренда',
    )
    banner_color = models.CharField(
        max_length=32,
        default='#3391c5',
        null=True,
        verbose_name='Цвет баннера бренда'
    )
    slug = models.SlugField(
        unique=True,
        max_length=128,
        db_index=True,
        verbose_name='url-адрес'
    )

    class Meta:
        ordering = ['place']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def get_absolute_url(self):
        return reverse('brand', kwargs={'brand_slug': self.slug})

    def __str__(self):
        return self.name.upper()



class Specialist(models.Model):
    name = models.CharField(max_length=56, verbose_name='Имя специалиста')
    phone = models.CharField(max_length=28, verbose_name='Телефон')
    email = models.EmailField(max_length=56, verbose_name='Email')

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

    def __str__(self):
        return self.name





class Category(BaseFields):
    def check_if_category_is_final(self):
        if self.parents.filter(parent__isnull=False).exists():
            self.is_final = True
            self.save(update_fields=['is_final'])

    @classmethod
    def post_save(cls, instance, created, updated, using, force_update, *args, **kwargs):
        if created:
            cls.check_if_category_is_final(instance)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    name = models.CharField(
        max_length=256,
        verbose_name='Название категории | Заголовок'
    )

    characteristics = RichTextField(
        default='',
        null=True,
        blank=True,
        verbose_name='Характеристики',
        config_name='default'
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Бренд, к которому относится категория'
    )
 
    parents = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name='Родительские категории',
        related_name='children',
        symmetrical=False
    )
    
    logo = models.ImageField(
        upload_to='category/logo',
        default='',
        null=True,
        blank=True,
        verbose_name='Логотип категории'
    )
    banner = models.ImageField(
        upload_to='category/banner',
        default='',
        blank=True,
        verbose_name='Баннер категории'
    )
    slug = models.SlugField(
        unique=True,
        max_length=128,
        db_index=True,
        verbose_name='url-адрес'
    )
    title = models.TextField(
        default='',
        null=True,
        blank=True,
        verbose_name='Title страницы'
    )

    keywords = models.TextField(
        default='',
        null=True,
        blank=True,
        verbose_name='Ключевые слова'
    )
        
    is_final = models.BooleanField(
        default=False,
        verbose_name='Отметка о том, что категория является финальной и в ней содержатся товары'
    )

    video_file = models.FileField(
        upload_to='category/videos',
        null=True,
        blank=True,
        verbose_name='Видео файл'
    )
    youtube_link = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Ссылка на YouTube'
    )
    rt_link = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Ссылка Rutube'
    )

    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Специалист, ответственный за категорию'
    )

    ru = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Номер РУ'
    )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['place']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        if self.brand:
            return str(self.brand).upper() + '----' + self.name.upper()
        return 'ПОДБОРКА' + '----' + self.name.upper()
    
class ProductManager(models.Manager):
    def get_queryset(self):
      return super().get_queryset().filter(is_final=True)


class Product(Category):
    objects = ProductManager()

    def save(self, *args, **kwargs):
        self.is_final = True  
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return super().get_absolute_url()


class Offer(BaseFields):
    name = models.CharField(
        max_length=128,
        verbose_name='Артикул'
    )
    text_description = models.TextField(
        default='',
        null=True,
        blank=True,
        verbose_name='Краткое описание (текст)',
    )
    text_full_description = models.TextField(
        default='',
        null=True,
        blank=True,
        verbose_name='Полное описание (текст)',
    )
    shipping_pack = models.CharField(
        max_length=10,
        verbose_name="Количество в упаковке",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='offer',
        verbose_name='Категория, к которой принадлежит товар'
    )

    characteristics = models.FileField(
        upload_to='characteristics/',  # Папка для сохранения файлов характеристик
        default='',
        null=True,
        blank=True,
        verbose_name='Характеристики',
    )
    tech_info = models.FileField(
        upload_to='files/instructions',
        null=True,
        blank=True,
        verbose_name='Техзадание'
    )
    ctru = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name='КТРУ'
    )

    class Meta:
        ordering = ['place']
        verbose_name = 'Код'
        verbose_name_plural = 'Коды'

    def __str__(self):
        return self.name


