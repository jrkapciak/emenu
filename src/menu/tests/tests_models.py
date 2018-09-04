from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from menu.models import Dish, Card


class DishTest(TestCase):
    """ Test module for Dish model """

    def setUp(self):
        self.dish = self.create_dish()

    @staticmethod
    def create_dish(name="Test Dish", description="description",
                    price=312, preparation_time=21):

        return Dish.objects.create(
            name=name,
            description=description,
            price=price,
            preparation_time=preparation_time,)

    def test_dish_creation(self):
        dish = self.create_dish()
        self.assertTrue(isinstance(dish, Dish))

    def test_vegan_value(self):
        # By default vegan field should be None
        self.assertEqual(self.dish.vegan, None)

    def test_vegan_set_invalid_value(self):
        self.dish.vegan = 'azeroth'
        with self.assertRaises(ValidationError):
            self.dish.save()

    def test_max_length_of_fields(self):
        descr_max_length = self.dish._meta.get_field('description').max_length
        name_max_length = self.dish._meta.get_field('name').max_length
        self.assertEqual(descr_max_length, 600)
        self.assertEqual(name_max_length, 255)


class CardTest(TestCase):
    """ Test module for Dish model """

    @classmethod
    def setUpTestData(cls):
        cls.dish = DishTest.create_dish()

    @staticmethod
    def create_card(name="Test Card 3", description="description 3"):
        return Card.objects.create(name=name, description=description)

    @staticmethod
    def add_dish(card, dish):
        card.dishes.add(dish)
        card.save()

    def setUp(self):
        self.card = self.create_card()

    def test_card_creation(self):
        self.assertTrue(isinstance(self.card, Card))

    def test_add_dish(self):
        self.add_dish(self.card, self.dish)
        self.assertEqual(self.card.dishes.all().first(), self.dish)

    def test_count_dish_no_dishes_case(self):
        self.assertEqual(self.card.count_dishes(), 0)

    def test_count_dish_2_dishes_case(self):
        dish2 = DishTest.create_dish(name="Test Dish 2",
                                     description="description"*10,
                                     price=112,
                                     preparation_time=51,
                                     )
        self.add_dish(self.card, self.dish)
        self.add_dish(self.card, dish2)
        self.assertEqual(self.card.count_dishes(), 2)

    def test_name_is_unique(self):
        self.create_card(name="Test Card", description="description 3")
        with self.assertRaises(IntegrityError):
            self.create_card(name="Test Card", description="description 3")

    def test_dishes_negative_value(self):
        # Dishes count should be greater than 0
        negative_dishes = -1
        card = self.create_card(name="Test Card",
                                description='Some text',
                                )
        with self.assertRaises(IntegrityError):
            card.dishes_count = negative_dishes
            card.save()

    def test_max_length_of_fields(self):
        descr_max_length = self.card._meta.get_field('description').max_length
        name_max_length = self.card._meta.get_field('name').max_length
        self.assertEqual(descr_max_length, 600)
        self.assertEqual(name_max_length, 255)




