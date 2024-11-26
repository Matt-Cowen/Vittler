from . import views
from django.urls import path

urlpatterns = [
    path('library/', 
        views.RecipeList.as_view(), name='library'),
    path ('',
        views.HomeView.as_view(), name='home'),
]
