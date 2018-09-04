from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Card, Dish
from .serializers import CardsSerializer, DishSerializer


class CardList(generics.ListAPIView):
    """
    List of all cards
     - padding defined in settings.py (4)
     - displays only Cards which contains at least one dish
     - ordered by card id (default) other options are:
            - name
            - number of associated dishes
    """
    queryset = Card.objects.filter(dishes_count__gt=0)
    serializer_class = CardsSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('name', 'dishes_count')
    ordering = ('id',)


class CardDetails(generics.RetrieveAPIView):
    """
    Details of chosen Card
    """
    queryset = Card.objects.all()
    serializer_class = CardsSerializer


class DishDetails(generics.RetrieveAPIView):
    """
    Details of dish
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
