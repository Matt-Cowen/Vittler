# Generated by Django 4.2.7 on 2024-11-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_library', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='serves',
            field=models.IntegerField(null=True),
        ),
    ]