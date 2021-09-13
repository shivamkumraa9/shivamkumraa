from django.db import models

class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    meta_description = models.CharField(max_length=255)

    def get_short_description(self):
        return self.content[:192]
    
    def get_json(self):
        return {
            "title": self.title,
            "slug": self.slug,
            "meta_description": self.meta_description
        }

    def __str__(self):
        return self.title

class BlogImage(models.Model):
    image = models.ImageField(upload_to="blog_images/")

    def __str__(self):
        return self.image.url
