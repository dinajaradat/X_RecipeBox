from django.db import models
from accounts.models import CustomUser

# Create your models here.
class recipe(models.Model):
    name = models.CharField(max_length=255,null=False)
    purchaser = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    recipe_box=models.TextField()

