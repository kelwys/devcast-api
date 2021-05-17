from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from ..paginations import CustomPagination
from ..serializers.episode_serializer import EpisodeSerializer
from ...models import Episode


class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['published_at', 'id']
    ordering = ['-published_at']
    pagination_class = CustomPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.queryset

    def get_serializer_class(self):
        return EpisodeSerializer
