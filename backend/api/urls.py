from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views_recipes import IngredientsViewSet, RecipeViewSet, TagsViewSet
from .views_user import CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'tags', TagsViewSet)
router.register(r'ingredients', IngredientsViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/me/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
