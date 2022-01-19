from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='название тeга')
    color = models.CharField(max_length=7, verbose_name='цвет тeга',)
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name='слаг тeга')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    measurement_unit = models.CharField(max_length=200,
                                        verbose_name='единица измерения')


class Recipe(models.Model):
    tags = models.ManyToManyField(Tag, verbose_name='Тeг')
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='recipes',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through="IngredientAmount",
        verbose_name="Ингредиенты",
        related_name="recipes",
    )
    name = models.CharField(verbose_name="Название", max_length=100)
    image = models.ImageField(verbose_name="Изображение", upload_to="recipes/")
    text = models.TextField(verbose_name="Описание")
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name="Время приготовления (мин.)"
    )
    pub_date = models.DateTimeField(
        "date published", auto_now_add=True, db_index=True
    )


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name="Ингридиент",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name="Рецепт",
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name="Количество",
    )


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="Рецепт",
    )


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name="Пользователь",
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name="Рецепт",
    )
