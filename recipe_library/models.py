from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

DIETARY_CHOICES = ((1, 'Vegetarian'),
               (2, 'Vegan'),
               (3, 'Gluten Free'),
               (4, 'Lactose Free'),
               (5, 'Nut free'))

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.

class Recipe(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    blurb = models.CharField(max_length=300, unique=True)
    creator = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="recipes"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField()
    method = models.TextField(blank=True)
    dietary_choices = MultiSelectField(choices=DIETARY_CHOICES,
                                 max_choices=5,
                                 max_length=5)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return f"{self.title} | from {self.creator}"