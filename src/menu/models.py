from django.db import models
from django.utils.translation import ugettext_lazy as _


class Dish(models.Model):

    name = models.CharField(max_length=255,  verbose_name=_('Name'))
    description = models.TextField(max_length=600,
                                   blank=True, verbose_name=_('Description'))
    price = models.DecimalField(
                        max_digits=6, decimal_places=2, null=True,
                        blank=True, help_text=_('Price in Polish zloty'),
                        verbose_name=_('Price'))
    preparation_time = models.PositiveSmallIntegerField(
                        null=True, blank=True, verbose_name=_('Preparation time'),
                        help_text=_('Time in minutes needed to prepare a meal'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vegan = models.NullBooleanField(verbose_name=_('Vegan dish'))

    class Meta:
        ordering = ['id']
        verbose_name = _('Dish')
        verbose_name_plural = _("Dishes")

    def __str__(self):
        return f"""{self.name} - {self.description[:60]} -
                {self.price} - {self.preparation_time} min"""


class Card(models.Model):

    name = models.CharField(max_length=255, unique=True, verbose_name=_('Name'))
    dishes = models.ManyToManyField(Dish, blank=True, related_name='cards',
                                    verbose_name=_('Dishes'))
    description = models.TextField(max_length=600, blank=True,
                                   verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dishes_count = models.PositiveSmallIntegerField(default=0,
                                                    verbose_name=_('number of dishes'))

    class Meta:
        ordering = ['id']
        verbose_name = _('Card')
        verbose_name_plural = _("Cards")

    def __str__(self):
        return f"""{self.name} - {self.description[:60]}"""

    def count_dishes(self):
        # Counts dishes associated with card
        return self.dishes.all().count()


