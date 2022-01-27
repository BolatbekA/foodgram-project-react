from django.contrib import admin

from .models import Follow, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    empty_value_display = '-empty-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'user')
    list_filter = ('author', 'user')
    search_fields = ('author', 'user')
    empty_value_display = '-empty-'
