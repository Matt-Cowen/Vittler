from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.utils.text import slugify
from .models import Recipe
from .forms import RecipeForm


class HomeView(generic.TemplateView):
    template_name = "recipe_library/index.html"


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipe_library/library.html"
    paginate_by = 1000

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_list'] = [
            (recipe, RecipeForm(instance=recipe)) for recipe in context['object_list']
        ]
        return context


def submit_recipe(request):

    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.creator = request.user
            recipe.slug = slugify(recipe.title)
            recipe.created_on = timezone.now()
            recipe.status = 1
            recipe.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Recipe submitted for approval!'
            )
            return redirect('submit_recipe')  # Redirect after success
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
        recipe_form = RecipeForm(data=request.POST, instance=recipe)
        if recipe_form.is_valid() and recipe.creator == request.user:
            recipe.save()
            messages.add_message(request, messages.SUCCESS, 'Recipe edited!')
            return redirect('library')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating recipe!')
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





    