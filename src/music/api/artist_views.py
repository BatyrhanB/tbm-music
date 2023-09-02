from rest_framework import generics, permissions


from music.services.artist_services import ArtistService
from music.serializers.artist_serializers import ArtistListSerializer, ArtistDetailSerializer


class ArtistAPIView(generics.ListAPIView):
    serializer_class = ArtistListSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return ArtistService.get_all_artists(is_deleted=False)


class ArtistDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ArtistDetailSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = "id"

    def get_queryset(self):
        return ArtistService.get_all_artists(is_deleted=False)
