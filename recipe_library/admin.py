from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'creator', 'created_on')
    search_fields = ['title', 'content', 'dietary_choices']
    list_filter = ('status', 'created_on', 'dietary_choices')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.