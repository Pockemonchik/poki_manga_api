from rest_framework import serializers
from .models import *


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'


class MangaQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=False,help_text="имя записи")


class TranscriberPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'

class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = '__all__'