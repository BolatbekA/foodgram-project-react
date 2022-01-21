from django.contrib import admin

from .models import User, Follow


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name")
    list_filter = ("username", "email")
    empty_value_display = "-empty-"


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "user")
    list_filter = ("author", "user")
    search_fields = ("user",)
    empty_value_display = "-пусто-"
