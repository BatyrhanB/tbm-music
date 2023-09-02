from django.urls import path

from music.api.song_views import SongListAPIView, SongDetailAPIView 

urlpatterns = [
    path("list/", SongListAPIView.as_view(), name="song-list"),
    path("detail/<uuid:id>/", SongDetailAPIView.as_view(), name="song-detail"),
]
