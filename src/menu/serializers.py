from rest_framework import serializers

from .models import Card, Dish


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'price',
                  'preparation_time', 'created_at', 'created_at',
                  'updated_at', 'vegan'
                  )


class CardsSerializer(serializers.ModelSerializer):

    # Dishes field represents dishes connected to certain card
    dishes = DishSerializer(read_only=True, many=True)

    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'dishes_count',
                  'dishes', 'created_at', 'created_at'
                  )




