from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.utils.text import slugify
from .models import Recipe, MyRecipes
from .forms import RecipeForm


class HomeView(generic.TemplateView):
    template_name = "recipe_library/index.html"


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipe_library/library.html"
    paginate_by = 12


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_list'] = [
            (recipe, RecipeForm(instance=recipe)) for recipe in context['object_list']
        ]
        return context

class MyRecipeList(generic.ListView):
    queryset = MyRecipes.objects.all()
    template_name = "recipe_library/my_recipes.html"
    context_object_name = "my_recipes_list"
    paginate_by = 12

    def get_queryset(self):
        my_recipes = MyRecipes.objects.filter(user=self.request.user).first()
        return my_recipes.recipe.all() if my_recipes else []

def add_to_my_recipes(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    my_recipes, created = MyRecipes.objects.get_or_create(user=request.user)
    if recipe in my_recipes.recipe.all():
        messages.info(request, "This recipe is already in your list!")
    else:
        # Add the recipe to the user's MyRecipes
        my_recipes.recipe.add(recipe)
        messages.success(request, "Recipe added to your list successfully!")
    return redirect('library')


def submit_recipe(request):

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        recipe_form.fields['prep_time'].label = "Preparation Time (mins)"
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.creator = request.user
            recipe.slug = slugify(recipe.title)
            recipe.created_on = timezone.now()
            recipe.status = 1
            recipe.save()
            messages.add_message(request, messages.SUCCESS, 'Recipe added!')
            return redirect('library')  # Redirect after success
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error submitting recipe!')
    else:
        recipe_form = RecipeForm()

    return render(
        request,
        'recipe_library/submit_recipe.html',
        {
            'recipe_form': recipe_form
        },
)



def recipe_edit(request, recipe_id):

    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        recipe_form.fields['prep_time'].label = "Preparation Time (mins)"
        if recipe_form.is_valid() and recipe.creator == request.user:
            recipe.save()
            messages.success(request, 'Recipe edited!')
            return redirect('library')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error editing recipe!')
    else:
        recipe_form = RecipeForm(instance=recipe)

    return render(
        request,
        "recipe_library/library.html",
        {
            'recipe_form': recipe_form,
            'recipe': recipe
        },
        )


def recipe_delete(request, recipe_id):
    
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    
    if recipe.creator == request.user:
        recipe.delete()
        messages.add_message(request, messages.SUCCESS, 'Recipe succesfully deleted')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own recipes!')

    return redirect('library')



def recipe_remove(request, recipe_id):
    
    recipe = get_object_or_404(MyRecipes, recipe=recipe_id)
    
    if recipe.creator == request.user:
        recipe.delete()
        messages.add_message(request, messages.SUCCESS, 'Recipe succesfully removed from your list')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own recipes!')

    return redirect('my_recipes')



    