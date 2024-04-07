from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=7, unique=True)
    slug = models.SlugField(unique=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    measurement_unit = models.CharField(max_length=256)


class IngredientInstance(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.IntegerField()


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256)
    tags = models.ManyToManyField(Tag, related_name='recipes')


class RecipeInstance(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_images', default='recipe_images/default.jpg')
    cooking_time = models.IntegerField()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
