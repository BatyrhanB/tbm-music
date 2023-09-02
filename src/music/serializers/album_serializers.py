from rest_framework import serializers

from music.models import Album, Artist, AlbumSong, Song


class AlbumListSerializer(serializers.ModelSerializer):
    artist_full_name = serializers.CharField(source="artist.full_name")

    class Meta:
        model = Album
        fields = ("id", "artist_full_name", "title", "release")


class ArtistInnerAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "full_name", "created_at", "updated_at")


class SongsTrackersSongInnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("id", "title")


class AlbumSongsTracksSerializer(serializers.ModelSerializer):
    song = SongsTrackersSongInnerSerializer(many=False)

    class Meta:
        model = AlbumSong
        fields = ("song", "track_number")


class AlbumDetailSerializer(serializers.ModelSerializer):
    artist = ArtistInnerAlbumSerializer(many=False)
    song_tackers = AlbumSongsTracksSerializer(many=True)

    class Meta:
        model = Album
        fields = ("id", "artist", "title", "release", "song_tackers", "created_at", "updated_at")
