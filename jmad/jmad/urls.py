from django.conf.urls import include, url
from django.contrib import admin

from solos import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
]
