
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipemanage import views


router = DefaultRouter()
router.register('list', views.RecipeListView, base_name='list')
router.register('add', views.RecipeCreateView, base_name='records')
router.register('delete', views.RecipeDetailsAPIView, base_name='delete')
router.register('update', views.RecipeUpdateAPIView, base_name='update')
router.register('view', views.RecipeDetailAPIView, base_name='view')

app_name = 'recipemanage'

urlpatterns = [
    path('', include(router.urls))
]
