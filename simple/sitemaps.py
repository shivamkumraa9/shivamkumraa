from django.contrib.sitemaps import Sitemap
from blog.models import Blog
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings

class BlogListSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        objects = Blog.objects.all()
        paginator = Paginator(objects, settings.ARTICLE_PAGINATE_BY)
        return paginator.page_range
    
    def location(self, page):
        return reverse("blog:blog", kwargs={"page": page})


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.created
    
    def location(self, obj):
        return reverse("blog:single_blog", kwargs={"slug": obj.slug})

class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['simple:index', 'simple:contact', 'simple:terms', 'simple:privacy']

    def location(self, item):
        return reverse(item)
