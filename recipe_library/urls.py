from . import views
from django.urls import path

urlpatterns = [
    path('library/', 
        views.RecipeList.as_view(), name='library'),
    path ('',
        views.HomeView.as_view(), name='home'),
    path ('submit_recipe/',
        views.submit_recipe, name='submit_recipe'),
    path('library/edit_recipe/<int:recipe_id>/',
         views.recipe_edit, name='recipe_edit'), 
    path('library/delete_recipe/<int:recipe_id>/',
         views.recipe_delete, name='recipe_delete'),    
]
