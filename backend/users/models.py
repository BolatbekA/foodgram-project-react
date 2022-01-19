from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import AppUserManager


class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        error_messages={
            'unique': ("User с таким email уже существует."),
        },
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        error_messages={
            'unique': ("User с таким username уже существует."),
        },
    )
    first_name = models.CharField(
        max_length=150,
        blank=False,
    )
    last_name = models.CharField(
        max_length=150,
        blank=False,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name", "username")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = AppUserManager()

    class Meta:
        ordering = ['date_joined']


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Подписчик",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Автор",
    )

    class Meta:
        ordering = ["-id"]
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "author"],
                name="unique follow",
            )
        ]
