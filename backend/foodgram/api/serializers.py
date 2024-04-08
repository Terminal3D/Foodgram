from rest_framework import serializers

from backend.recipes.models import Tag


class TagSerializer(serializers.Serializer):

    class Meta:
        model = Tag
        fields = ('pk', 'name', 'color', 'slug')
