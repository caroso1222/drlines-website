from django.conf.urls import url
from django.views.generic import TemplateView
from pruebauser import views

urlpatterns = [
    url(r'^$', views.home, name ="home"),
    url(r'^user/', views.userHome, name ="user"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/test/'}),
]