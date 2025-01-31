from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from catalog.models import Category, Product, Brand, Offer

class IndexSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Category.visible.filter(is_final=False).all()

    def location(self, obj):
        return reverse('category', args=[obj.slug])

class OfferSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
         return Offer.visible.all() # Получаем все предложения

    def location(self, obj):
         # Получаем бренд из категории, связанной с предложением
         if obj.category and obj.category.brand:
            brand_slug = obj.category.brand.slug
         else:
            return '' # возвращаем пустую строку, если нет бренда

         return reverse('offer', args=[brand_slug, obj.category.slug]) # Передаем brand_slug и category_slug

class BrandSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Brand.visible.all()

    def location(self, obj):
        return reverse('brand', args=[obj.slug])

sitemaps = {
    'index': IndexSitemap,
    'categories': CategorySitemap,
    'offers': OfferSitemap,
    'brands': BrandSitemap,
}
