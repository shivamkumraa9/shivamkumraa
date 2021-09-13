from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.views.generic.base import TemplateView

from simple.sitemaps import BlogSitemap, StaticSitemap, BlogListSitemap

sitemaps = {
    'blog_list': BlogListSitemap,
    'blog': BlogSitemap,
    'static': StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simple.urls')),
    path('blog/', include('blog.urls')),

    # Seo Stuff
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(
        template_name="simple/robots.txt", content_type="text/plain")
    ),  #add the robots.txt file

]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
