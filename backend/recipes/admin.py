from django.contrib import admin

from .models import Tag, Ingredient, Recipe, Favorite, ShoppingCart, Subscription, RecipeIngredient


class RecipeIngredientsInLine(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeIngredientsAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientsInLine]


admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeIngredientsAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
admin.site.register(Subscription)
