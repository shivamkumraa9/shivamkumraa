from django.contrib import admin
from blog.models import Blog, BlogImage

admin.site.register([Blog, BlogImage])
