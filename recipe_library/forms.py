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
    prep_time = forms.IntegerField(label="Preparation Time (minutes)")
    ingredients = forms.CharField(widget=forms.Textarea(attrs={"rows":5}), label="Ingredients (new line for each ingredient)")


