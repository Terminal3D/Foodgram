from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=7, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    measurement_unit = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, related_name='ingredient_recipes')
    amount = models.CharField(max_length=100)

    def __str__(self):
        return "Recipe: " + self.recipe.__str__() + " Ingredient: " + self.ingredient.__str__()

    class Meta:
        unique_together = ('recipe', 'ingredient')


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_recipes')
    title = models.CharField(max_length=256)
    tags = models.ManyToManyField(Tag, related_name='tagged_recipes', blank=True)
    ingredients = models.ManyToManyField(Ingredient, through=RecipeIngredient, related_name='recipes')
    description = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to='recipe_images', default='recipe_images/default.jpg')
    cooking_time = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorite_by')

    def __str__(self):
        return self.recipe.__str__() + " by " + self.user.__str__()


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_cart')
    recipes = models.ManyToManyField(Recipe, related_name='in_shopping_carts')

    def __str__(self):
        return self.user


class SubscriptionManager(models.Manager):
    def is_subscribed(self, user, author):
        return Subscription.objects.filter(subscriber=user, author=author).exists()

    def get_subscriptions(self, user):
        return user.subscriptions.all()

    def get_subscribers(self, user):
        return user.subscribers.all()


class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    object = SubscriptionManager()

    def __str__(self):
        return self.author.__str__() + " followed by" + self.subscriber.__str__()
