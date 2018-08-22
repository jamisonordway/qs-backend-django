import json
from api.models import Food
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase

class ModelTestCase(TestCase):
  """Defines the test suite for the food model."""

  def setUp(self):
    """Define test client and other test variables."""
    self.food_name = "Pizza"
    self.food_calories = 300
    self.food = Food(name=self.food_name, calories=self.food_calories)

def test_model_can_create_a_food(self):
    """Test the food model can create a food."""
    count = Food.objects.count()
    self.food.save()
    new_count = Food.objects.count()
    self.assertNotEqual(count, new_count)

class FoodViewsTest(TestCase):
  """Test suite for the food api views."""

  def setUp(self):
    """Define the test client and other test variables."""
    self.client = APIClient()
    self.chorizo = Food.objects.create(name="chorizo", calories=200)
    self.ramen = Food.objects.create(name="ramen", calories=500)

  def test_status_for_all_foods(self):
    response = self.client.get("/api/v1/foods")
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_gets_all_foods(self):
    response = self.client.get("/api/v1/foods")
    js = response.json()
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(js), 2)
    self.assertEqual(js[0]["name"], self.chorizo.name)
    self.assertEqual(js[0]["calores"], self.chorizo.calories)
    self.assertEqual(js[1]["name"], self.ramen.name)
    self.assertEqual(js[1]["calories"], self.oatmeal.calories)