# Generated by Django 4.2.7 on 2024-11-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_library', '0006_alter_recipe_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='featured_image',
            field=models.ImageField(blank=True, default='placeholder', null=True, upload_to='../static/images/'),
        ),
    ]
