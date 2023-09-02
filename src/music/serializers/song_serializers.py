from rest_framework import serializers

from music.models import Song, Artist


class SongListSerializer(serializers.ModelSerializer):
    artist_full_name = serializers.CharField(source="artist.full_name")

    class Meta:
        model = Song
        fields = ("id", "artist_full_name", "title")


class SongArtistInnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "full_name", "created_at", "updated_at")


class SongDetailSerializer(serializers.ModelSerializer):
    artist = SongArtistInnerSerializer(many=False)

    class Meta:
        model = Song
        fields = ("id", "artist", "title", "created_at", "updated_at")
