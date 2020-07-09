from django.conf.urls import include, url
from django.contrib import admin

from solos import views
from solos.views import SoloDetailView


urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^solos/(?P<pk>\d+)/$', SoloDetailView.as_view()),
]
