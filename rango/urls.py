from django.conf import settings # New Import
from django.conf.urls.static import static # New Import
from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'))


if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
