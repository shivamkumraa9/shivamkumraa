from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('<int:page>/', views.blog, name='blog'),
    path('pagination/<int:page>/', views.blog_pagination, name='pagination'),
    path('<slug:slug>/', views.single_blog, name='single_blog'),
    
]
