from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

DIETARY_CHOICES = ((1, 'Vegetarian'),
               (2, 'Vegan'),
               (3, 'Gluten Free'),
               (4, 'Lactose Free'),
               (5, 'Nut free'))

STATUS = ((0, "Under review"), (1, "Published"))


# Create your models here.

class Recipe(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    blurb = models.CharField(max_length=300, unique=True)
    creator = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="recipes"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    serves = models.IntegerField(null=True)
    prep_time = models.IntegerField(null=True)
    ingredients = models.TextField()
    method = models.TextField()
    dietary_choices = MultiSelectField(choices=DIETARY_CHOICES, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return f"{self.title} | from {self.creator}"


class MyRecipes(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="myrecipes"
    )
    recipe = models.ManyToManyField(Recipe)
    context_object_name = "my_recipes_list"
