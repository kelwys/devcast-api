from rest_framework import serializers

from .file_serializer import FileSerializer
from ...models import Episode


class EpisodeSerializer(serializers.ModelSerializer):
    file = FileSerializer(many=False)

    class Meta:
        model = Episode
        fields = '__all__'
