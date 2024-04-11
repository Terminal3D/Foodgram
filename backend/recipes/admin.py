from django.contrib import admin
from .models import Tag, Ingredient, Recipe, Favorites, ShoppingCart, Subscriptions, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, ]
    list_display = ('name', 'author', 'cooking_time')
    search_fields = ['name', 'text', 'author__username']
    list_filter = ('tags', 'author')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ['name']


@admin.register(Favorites)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'list_recipes')
    search_fields = ['user__username', 'recipe__name']

    def list_recipes(self, obj):
        return ", ".join([recipe.name for recipe in obj.recipes.all()])

    list_recipes.short_description = 'Recipes'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'list_recipes')
    search_fields = ['user__username', 'recipe__name']

    def list_recipes(self, obj):
        return ", ".join([recipe.name for recipe in obj.recipes.all()])

    list_recipes.short_description = 'Recipes'


@admin.register(Subscriptions)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'list_subscriptions')
    search_fields = ['user__username', 'subscription__username']

    def list_subscriptions(self, obj):
        return ", ".join([user.username for user in obj.subscription.all()])

    list_subscriptions.short_description = 'Subscriptions'
