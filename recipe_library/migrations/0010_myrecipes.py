# Generated by Django 4.2.7 on 2024-12-05 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe_library', '0009_alter_recipe_dietary_choices_alter_recipe_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ManyToManyField(to='recipe_library.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myrecipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]