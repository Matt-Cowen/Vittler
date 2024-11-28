from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """
    Form class for users to add their own recipe
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Recipe
        fields = ('title', 'featured_image', 'blurb', 'serves', 'prep_time', 'ingredients', 'method', 'dietary_choices',)

            