from rest_framework import serializers

from music.models import Artist


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "full_name")


class ArtistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "full_name", "created_at", "updated_at")