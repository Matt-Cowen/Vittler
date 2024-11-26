from django.shortcuts import render, get_object_or_404, reverse
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


def recipe_submit(request):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    queryset = Recipe.objects.all()

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
    
    recipe_form = RecipeForm()

    return render(
        request,
        "recipe_library/submit_recipe.html",
        {
            'recipe_form': recipe_form
        },
)