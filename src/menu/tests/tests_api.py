import string
import random

from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from menu.models import Dish, Card
from menu.views_api import CardList
from .tests_models import CardTest, DishTest


def random_generator(size=None, chars=string.ascii_uppercase + string.digits):
    if size:
        return ''.join(random.choice(chars) for _ in range(size))
    return ''.join(random.choice(chars) for _ in range(random.randint(1, 50)))


class CardListTest(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(CardListTest, cls).setUpClass()
        cls.number_of_cards = 24
        for i in range(cls.number_of_cards):
            CardTest.create_card(name=random_generator(), description=random_generator())

    def test_get_right_amount_of_cards(self):
        """
        Ensure we can get a list of all Cards (24)
        """
        self.assertEqual(Card.objects.count(), self.number_of_cards)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/cards/1/')  # for 1st Card
        self.assertEqual(response.status_code, 200)

    def test_card_detail_view_returns_dishes(self):
        CardTest.create_card(name=random_generator(), description=random_generator())
        test_dish_name = random_generator(32)
        test_dish_description = random_generator(12)

        dish = DishTest.create_dish(name=test_dish_name, description=test_dish_description)
        card = Card.objects.get(pk=1)
        card.dishes.add(dish)
        card.save()

        first_dish = self.client.get('/cards/1/').data.get('dishes')[0]
        first_dish_name = first_dish.get('name')
        first_dish_descr = first_dish.get('description')

        self.assertEqual(test_dish_name, first_dish_name)
        self.assertEqual(test_dish_description, first_dish_descr)













