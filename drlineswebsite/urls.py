from django.conf.urls import include, url
from django.contrib import admin
from main import views
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'drlineswebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name = 'home'),
    url(r'^test/', include('pruebauser.urls'), name = 'home'),

    url(r'^pedir/', TemplateView.as_view(template_name="pedir.html")),
]
