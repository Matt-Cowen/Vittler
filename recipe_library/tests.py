from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe, MyRecipes
from .forms import RecipeForm


"""
Tests for Views
"""

class RecipeViewsTestCase(TestCase):

    def setUp(self):
        ## Test Users
        self.user = User.objects.create_user(username="testuser", password="password")
        self.other_user = User.objects.create_user(username="otheruser", password="password")


        ##Test Recipes
        self.recipe1 = Recipe.objects.create(
            title="Test Recipe 1",
            slug="test-recipe-1",
            blurb="Delicious recipe 1",
            ingredients="Sugar, Spice",
            method="All Things Nice",
            serves=2,
            prep_time=20,
            creator=self.user,
            status=1,
        )
        self.recipe2 = Recipe.objects.create(
            title="Test Recipe 2",
            slug="test-recipe-2",
            blurb="Delicious recipe 2",
            ingredients="Flour, Butter",
            method="Eggs",
            serves=2,
            prep_time=20,
            creator=self.user,
            status=1,
        )
        


    def test_recipe_list_view(self):
        response = self.client.get(reverse("library"))

        self.assertTemplateUsed(response, "recipe_library/library.html")
        self.assertContains(response, self.recipe1.title)
        self.assertContains(response, self.recipe2.title)

    def test_recipe_list_view_search(self):
        response = self.client.get(reverse("library") + "?search=Sugar")

        self.assertContains(response, self.recipe1.title)
        self.assertNotContains(response, self.recipe2.title)


    def test_add_to_my_recipes(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("add_to_my_recipes", args=[self.recipe1.id]))
        self.assertRedirects(response, reverse("library"))

        my_recipes = MyRecipes.objects.get(user=self.user)
        self.assertIn(self.recipe1, my_recipes.recipe.all())

    def test_remove_from_my_recipes(self):
        my_recipes = MyRecipes.objects.create(user=self.user)
        my_recipes.recipe.add(self.recipe1)

        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("remove_from_my_recipes", args=[self.recipe1.id]))
        self.assertRedirects(response, reverse("my_recipes"))
        self.assertNotIn(self.recipe1, my_recipes.recipe.all())



"""
Tests for the Recipe Submission Form
"""
    
class RecipeFormTestCase(TestCase):

    def test_valid_recipe_form(self):
        form_data = {
            "title": "Test Recipe",
            "blurb": "A test recipe",
            "ingredients": "Salt, Pepper",
            "prep_time": 15,
            "serves": 4,
            "method": "Mix and cook",
        }
        form = RecipeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_recipe_form_missing_title(self):
        form_data = {
            "blurb": "A test recipe",
            "ingredients": "Salt, Pepper",
            "prep_time": 15,
            "serves": 4,
            "method": "Mix and cook"
        }
        form = RecipeForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
