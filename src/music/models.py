from django.db import models

from common.models import BaseModel


class Artist(BaseModel):
    full_name = models.CharField(max_length=155, null=False, blank=False, verbose_name="Full name")

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        db_table = "music__artists"
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        ordering = ("-created_at",)


class Album(BaseModel):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Artist", related_name="albums"
    )
    title = models.CharField(max_length=155, null=False, blank=False, verbose_name="Title")
    release = models.DateField(null=True, blank=True, verbose_name="Year of release")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "music__albums"
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ("-created_at",)


class Song(BaseModel):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Artist", related_name="songs"
    )
    title = models.CharField(max_length=155, null=False, blank=False, verbose_name="Title")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "music__songs"
        verbose_name = "Songs"
        verbose_name_plural = "Songs"
        ordering = ("-created_at",)


class AlbumSong(BaseModel):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Album", related_name="song_tackers"
    )
    song = models.ForeignKey(
        Song, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Song", related_name="song_tackers"
    )
    track_number = models.PositiveIntegerField(default=1, null=False, blank=False, verbose_name="Track number")

    def __str__(self):
        return f"{self.album}: Track number: {self.track_number}"

    class Meta:
        db_table = "music__songs__tack"
        verbose_name = "Song track"
        verbose_name_plural = "Song tracks"
        ordering = ("-created_at",)
