from django.contrib import admin

from .models import Cart, Favorite, Ingredient, Recipe, Tag, IngredientAmount


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'measurement_unit')
    search_fields = ('name',)
    empty_value_display = '-empty-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'color', 'slug')
    search_fields = ('name',)
    list_filter = ('name', 'slug')
    empty_value_display = '-empty-'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'favorite_count')
    search_fields = ('name', 'author', 'tags')
    list_filter = ('name', 'author', 'tags')
    empty_value_display = '-empty-'

    def favorite_count(self, obj):
        return Favorite.objects.filter(recipe=obj).count()


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    empty_value_display = '-empty-'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    empty_value_display = '-empty-'


@admin.register(IngredientAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'amount')
    empty_value_display = '-empty-'
