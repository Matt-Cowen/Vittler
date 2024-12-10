from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.utils.text import slugify
from django.db.models import Q 
from .models import Recipe, MyRecipes
from .forms import RecipeForm


class HomeView(generic.TemplateView):
    """
    Simple template display.

    **Template:**

    :template:`recipe_library/index.html`
    """
    template_name = "recipe_library/index.html"


class RecipeList(generic.ListView):

    """
     A view to display a paginated list of recipes in the Recipe Library.

    Returns either all published recipes or a filtered queryset
    based on the search parameters for recipes in the 
    :model:recipe_library.Recipe, and pairs each recipe with an editable form
    instance for rendering in the template.

    Attribs:

    ``queryset``
        Default queryset - all published recipes 
    ``paginate_by``
        Number of recipes per page


    Methods:

    ``get_context_data()``
        Adds context by pairing each recipe with its corresponding form instance, and 
        then returns a context dictionary with `recipe_list` variable representing a
        list of tuple pairs of (recipe, form)

    ``get_queryset()``
        Allows user to update queryset using a search query. Filters by matching string
        in recipe Title, Blurb and Ingredients

    **Template:**

    :template:`recipe_library/library.html`
    """

    queryset = Recipe.objects.filter(status=1)
    template_name = "recipe_library/library.html"
    paginate_by = 12



    def get_context_data(self, **kwargs):                   #Matches recipe to its instance of the form and passes it back as tuple.
        context = super().get_context_data(**kwargs)
        context['recipe_list'] = [
            (recipe, RecipeForm(instance=recipe)) for recipe in context['object_list']
        ]
        return context

    def get_queryset(self):                                  #Filters the queryset based on title, blurb, and ingredients containing search
        queryset = Recipe.objects.filter(status=1)  

        search_query = self.request.GET.get('search', '') 
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |  
                Q(blurb__icontains=search_query) | 
                Q(ingredients__icontains=search_query)
            )

        return queryset

class MyRecipeList(generic.ListView):

    """
    A view to display a paginated list of recipes in the current user's saved recipes.

    This view retrieves the recipes saved logged-in user, allowing users 
    to view and manage their saved recipes.

    Attribs:

        ``queryset (QuerySet)`` 
            The base queryset containing all instances of `MyRecipes`.
        ``context_object_name``
            The context variable name passed to the template for the recipe list.
        ``paginate_by``
            Number of recipes per page

    Methods:
        get_queryset():
            Returns a queryset of recipes saved by the user from the library. If the user does not 
            have a `MyRecipes` instance, an empty list is returned.


    Template:
        :template:`recipe_library/my_recipes.html`
    """


    queryset = MyRecipes.objects.all()
    template_name = "recipe_library/my_recipes.html"
    context_object_name = "my_recipes_list"
    paginate_by = 12

    def get_queryset(self):
        my_recipes = MyRecipes.objects.filter(user=self.request.user).first()
        return my_recipes.recipe.all() if my_recipes else []

def add_to_my_recipes(request, recipe_id):

    """
    Adds a recipe to the :model:`recipe_library.MyRecipes`.

    Allows users to add recipes to their list from the recipe library. If recipe is already in
    their list, message shown, otherwise recipe added and success message shown.

    **Context**

    ``request.user``
        The logged in user adding the recipe.
    ``my_recipes``
        The logged in user's instance of :model:`recipe_library.MyRecipes`
    ``recipe``
        The recipe being added, identified by ID

    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    my_recipes, created = MyRecipes.objects.get_or_create(user=request.user)
    if recipe in my_recipes.recipe.all():
        messages.info(request, "This recipe is already in your book!")
    else:
        my_recipes.recipe.add(recipe)
        messages.success(request, "Recipe added to your book")
    return redirect('library')

def remove_from_my_recipes(request, recipe_id):

    """
    Removes a recipe from the :model:`recipe_library.MyRecipes`.

    Allows users to remove recipes from their list of saved recipes.
    Displays message when recipe succesfully removed.

    **Context**

    ``request.user``
        The logged in user adding the recipe.
    ``my_recipes``
        The logged in user's instance of :model:`recipe_library.MyRecipes`
    ``recipe``
        The recipe being added, identified by ID

    """

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    my_recipes = MyRecipes.objects.get(user=request.user)
    my_recipes.recipe.remove(recipe)
    messages.success(request, "Recipe removed from your book")
    return redirect('my_recipes')


def submit_recipe(request):

    """
    Handles the submission of a new recipe to the recipe library by a user.
    On successful form submission, creates a new recipe instance with metadata
    for the recipe (creator, slug, created_on, status.) It then saves the recipe and redirects
    to the recipe library page.

    **Requests**
    GET
        Renders an empty recipe submission form.
    POST
        Validates and saves the submitted recipe form. If the form is valid, the recipe is 
        saved with the current user's information, and a success message is displayed. 
        Otherwise, an error message is shown.

    **Context**
        ``recipe_form``: An instance of :form:`recipe_library.RecipeForm`, either empty 
          (for GET requests) or populated with submitted data (for POST requests).


    Template:
        :template:`recipe_library/submit_recipe.html`.
    """

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


    """
    Handles the editing of a recipe instance by a user.

    On successful form submission, updates recipe instance with submitted data.
    It then saves the recipe and redirects to the recipe library page.

    **Requests**
    GET
        Renders recipe submission form populated with the data for the current recipe (passed in through args).
    POST
        Validates and saves the submitted recipe form, with similar functionality to the :method:`submit_recipe`

    **Context**
        ``recipe_form``: An instance of :form:`recipe_library.RecipeForm`, either 
            populated with data from the current recipe instance
          (for GET requests) or populated with submitted data (for POST requests).


    Template:
        :template:`recipe_library/recipe_edit.html`.
    """

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

    """
    Handles the deletion of a recipe by its creator.

    This view allows a logged-in user to delete a recipe they have created. 
    It validates that the user is the recipe's creator before deleting, and redirecting
    to the library page.

    """    
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    
    if recipe.creator == request.user:
        recipe.delete()
        messages.add_message(request, messages.SUCCESS, 'Recipe succesfully deleted')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own recipes!')

    return redirect('library')



    