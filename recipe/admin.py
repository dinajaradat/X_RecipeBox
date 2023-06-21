from django.contrib import admin
from .models import recipe
# Register your models here.
class CustomRecipeAdmin(admin.ModelAdmin):
    model = recipe
    list_display = ['name', 'purchaser','recipe_box',]

admin.site.register(recipe, CustomRecipeAdmin)