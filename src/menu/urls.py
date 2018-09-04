from django.conf.urls import url

from .views import menu
from .views_api import CardList, CardDetails, DishDetails

urlpatterns = [
    url(r'^$', menu, name='list'),  # Main view of app

    # API VIEWS
    url(r'^cards/$', CardList.as_view(), name='cards'),
    url(r'^cards/(?P<pk>[0-9]+)/$', CardDetails.as_view(), name='card'),
    url(r'^dish/(?P<pk>[0-9]+)/$', DishDetails.as_view(), name='dish'),
]