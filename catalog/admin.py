from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.urls import reverse



from catalog.models import Brand, Category, Offer, Specialist, Product
from files.models import ModelImage, ModelFile, InstructionsFile, CatalogFile
from catalog.admin_filters import DropdownFilter, RelatedOnlyDropdownFilter, CategoryRelatedOnlyDropdownFilter


"""Общие методы админки"""


class MyAdminSite(AdminSite):
    def get_app_list(self, request, app_label=None):
        """Возвращает отсортированный список зарегистрированных приложений"""
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        return app_list


admin.site = MyAdminSite()

admin.site.empty_value_display = '---- ОТСУТСТВУЕТ'


class OfferInline(admin.TabularInline):
    model = Offer
    can_delete = True
    extra = 0
    show_change_link = True
    classes = ['collapse', 'wide']


class CategoryImageInline(admin.TabularInline):
    model = ModelImage
    readonly_fields = ('image_preview',)

class CategoryFileInline(admin.TabularInline):
    model = ModelFile

class InstructionsFileInline(admin.TabularInline):
    model = InstructionsFile

class CatalogFileInline(admin.TabularInline):
    model = CatalogFile



""""Классы админки"""


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        'name',
        'slug',
        'place',
        'status',
        'banner_color'
    )
    list_editable = ('place', 'slug', 'status', 'banner_color')
    list_filter = (('name', DropdownFilter), 'status')
    fields = [
        'name',
        'description',
        'slug',
        'place',
        'status',
        'logo',
        'banner',
        'banner_color'
    ]
    view_on_site = True
    actions_on_bottom = True
    list_per_page = 25
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("name",)}
    list_select_related = ['brand']
    list_display = (
        'name',
        'brand',
        'slug',
        'place',
        'status',
        'is_final'
    )
    list_editable = ('place', 'slug', 'status')
    list_filter = (
        ('brand', RelatedOnlyDropdownFilter),
        ('parents', CategoryRelatedOnlyDropdownFilter),
        'status',
        'is_final'
    )
    fields = [
        'db_id',
        'name',
        'description',
        'full_description',
        'metadescription',
        'logo',
        'banner',
        'parents',
        'brand',
        'slug',
        'place',
        'status',
        'is_final',
        'video_file',
        'youtube_link',
        'rt_link',
        'specialist',
        'ru'
    ]
    filter_horizontal = ('parents', )
    autocomplete_fields = ('brand', )
    view_on_site = True
    actions_on_bottom = True
    list_per_page = 25
    search_fields = ['name']

   

    def get_form(self, request, obj=None, **kwargs):
        form = super(CategoryAdmin, self).get_form(request, obj, **kwargs)
        qs = form.base_fields['parents'].queryset
        form.base_fields['parents'].queryset = qs.select_related('brand').all()
        return form


class OfferAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = (
        'name',
        'brand_name',
        'category',
        'characteristics',
        'place',
        'status'
    )
    list_editable = ('place', 'status')
    list_filter = (
        ('category__brand', RelatedOnlyDropdownFilter),
        ('category', CategoryRelatedOnlyDropdownFilter),
        'status'
    )
    fields = [
        'name',
        'description',
        'characteristics',
        'shipping_pack',
        'tech_info',
        'ctru',
        'category',
        'place',
        'status'
    ]
    autocomplete_fields = ['category']
    actions_on_bottom = True
    list_per_page = 25
    search_fields = ['name']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category', 'category__brand')

    @admin.display(description='Бренд', ordering='name')
    def brand_name(self, obj):
        if getattr(obj, 'category'):
            if obj.category.brand:
                return obj.category.brand.name
        elif hasattr(obj, 'brand'):
            return obj.brand.name
        else:
            return "Бренда нет"

class OfferInline(admin.TabularInline):
    model = Offer
    can_delete = True
    extra = 0
    show_change_link = True
    classes = ['collapse', 'wide']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'is_final']
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['brand', 'is_final']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductImageInline(admin.TabularInline):
    model = ModelImage
    readonly_fields = ('image_preview',)
    
class ProductFileInline(admin.TabularInline):
    model = ModelFile

class InstructionsFileInline(admin.TabularInline):
    model = InstructionsFile
    
class CatalogFileInline(admin.TabularInline):
    model = CatalogFile

class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'is_final']
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['brand', 'is_final']
    search_fields = ['name']
    inlines = [OfferInline, ProductImageInline, ProductFileInline, InstructionsFileInline, CatalogFileInline]


admin.site.register(Brand, BrandAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)

admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Product, ProductAdmin)
