from django.contrib import admin
from .models import Tag, Ingredient, Recipe, Favorite, ShoppingCart, Subscription, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, ]
    list_display = ('name', 'author', 'cooking_time')
    search_fields = ['name', 'description', 'author__username']
    list_filter = ('tags', 'author')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ['name']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ['user__username', 'recipe__title']


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'list_recipes')
    search_fields = ['user__username']

    def list_recipes(self, obj):
        return ", ".join([recipe.title for recipe in obj.recipes.all()])

    list_recipes.short_description = 'Recipes'


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'author')
    search_fields = ['subscriber__username', 'author__username']
