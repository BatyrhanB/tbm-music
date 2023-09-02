from rest_framework import generics, permissions


from music.serializers.album_serializers import AlbumListSerializer, AlbumDetailSerializer
from music.services.album_services import AlbumService


class AlbumListAPIView(generics.ListAPIView):
    serializer_class = AlbumListSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return AlbumService.get_all_artists(is_deleted=False)


class AlbumDetailAPIView(generics.RetrieveAPIView):
    serializer_class = AlbumDetailSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = "id"

    def get_queryset(self):
        return AlbumService.get_all_artists(is_deleted=False)
