
from django.urls import include, path
from rest_framework import routers

from .api.viewsets.episode_viewset import EpisodeViewSet

router = routers.DefaultRouter()

router.register('episodes', EpisodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
