from rest_framework import generics, permissions

from music.serializers.song_serializers import SongListSerializer, SongDetailSerializer
from music.services.song_services import SongService


class SongListAPIView(generics.ListAPIView):
    serializer_class = SongListSerializer 
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return SongService.get_all_artists(is_deleted=False)


class SongDetailAPIView(generics.RetrieveAPIView):
    serializer_class = SongDetailSerializer 
    permission_classes = (permissions.AllowAny,)
    lookup_field = "id"

    def get_queryset(self):
        return SongService.get_all_artists(is_deleted=False)
