from . import views
from django.urls import path

urlpatterns = [
    path('library/', 
        views.RecipeList.as_view(), name='library'),
    path ('',
        views.HomeView.as_view(), name='home'),
    path('my_recipes/',
        views.MyRecipeList.as_view(), name='my_recipes'),
    path('my_recipes/add_recipe/<int:recipe_id>/',
        views.add_to_my_recipes, name='add_to_my_recipes'),
    path ('submit_recipe/',
        views.submit_recipe, name='submit_recipe'),
    path('library/edit_recipe/<int:recipe_id>/',
         views.recipe_edit, name='recipe_edit'), 
    path('library/delete_recipe/<int:recipe_id>/',
         views.recipe_delete, name='recipe_delete'),    
]
