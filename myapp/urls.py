from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.get_name, name='form'),
    url(r'^error404/', views.error404, name='404'),
)