from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'creator', 'created_on')
    search_fields = ['title', 'ingredients', 'dietary_choices']
    list_filter = ('status', 'creator', 'serves', 'prep_time', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'method')


# Register your models here.