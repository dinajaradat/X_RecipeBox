# Generated by Django 4.2 on 2023-06-21 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='desc',
            new_name='recipe_box',
        ),
    ]
