from django.conf.urls import include, url
from django.contrib import admin

from solos import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^recordings/(?P<album>[\w-]+)/(?P<track>[\w-]+)/(?P<artist>[\w-]+)/$',
        views.solo_detail, name='solo_detail_view'),
]
