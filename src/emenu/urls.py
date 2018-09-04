from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'', include('menu.urls', namespace='menu')),
]


urlpatterns += [
    url('i18n/', include('django.conf.urls.i18n')),
    url('admin/', admin.site.urls),
]
