from django.contrib import admin
from .models import Card, Dish


class CardAdmin(admin.ModelAdmin):
    model = Card

    def save_model(self, request, obj, form, change):
        # Used to populate dishes_count field with number of dishes related to card
        instance = form.save(commit=True)
        instance.dishes_count = instance.count_dishes()
        instance.save()
        return instance


class DishAdmin(admin.ModelAdmin):
    pass


admin.site.register(Card, CardAdmin)
admin.site.register(Dish, DishAdmin)
