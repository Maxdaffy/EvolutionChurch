from django.conf.urls import include, url, patterns
from . import views


urlpatterns = [
     url(r'^$', views.person, name='person'),
      url(r'^contact/$', views.contact, name='contact'),


]