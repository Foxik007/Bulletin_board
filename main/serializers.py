from rest_framework import serializers
from .models import Bb


class BbSerializers(serializers.ModelSerializer):
    rubric = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Bb
        fields = ['title', 'price', 'rubric']


class BbSerializersDetail(serializers.ModelSerializer):
    rubric = serializers.SlugRelatedField(slug_field='name', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Bb
        exclude = ['is_active', 'image']
