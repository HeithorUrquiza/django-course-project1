from django.urls import reverse, resolve
from recipes import views        
from .test_recipe_base import RecipeTestBase

class RecipeDetailViewTest(RecipeTestBase):
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipes)

    def test_recipe_detail_view_loads_correct_template(self):
        recipe = self.make_recipe()
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id}))
        self.assertTemplateUsed(response, 'recipes/pages/recipe-view.html')

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
        
    def test_recipe_detail_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.id})
        )
        self.assertEqual(response.status_code, 404)
