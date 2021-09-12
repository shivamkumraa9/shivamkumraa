from blog import views
from django.views.generic import TemplateView
from django.urls import path

TV = TemplateView.as_view

app_name="simple"

urlpatterns = [
    path('',  TV(template_name="simple/index.html"), name='index'),
    path('contact/',  TV(template_name="simple/contact.html"), name='contact'),
    path('terms/',  TV(template_name="simple/terms.html"), name='terms'),
    path('privacy/',  TV(template_name="simple/privacy.html"), name='privacy'),

]
