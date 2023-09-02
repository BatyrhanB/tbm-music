from django.contrib import admin


from music.models import Artist, Album, AlbumSong, Song


class AlbumInline(admin.TabularInline):
    model = Album
    fields = ["title", "release"]
    extra = 1


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("full_name", "created_at")
    list_display_links = ("full_name",)
    fields = (
        "full_name",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    search_fields = ["full_name"]
    ordering = ["-created_at"]
    list_per_page = 25
    inlines = [AlbumInline]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("artist", "title", "release")
    list_display_links = ("title",)
    fields = (
        "title",
        "artist",
        "release",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    search_fields = ["title"]
    ordering = ["-created_at"]
    list_per_page = 20


@admin.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
    list_display = ("track_number", "album", "song")
    list_display_links = ("track_number",)
    fields = (
        "track_number",
        "album",
        "song",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    search_fields = ["track_number"]
    ordering = ["-created_at"]
    list_per_page = 20


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "artist")
    list_display_links = ("title",)
    fields = (
        "title",
        "artist",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    search_fields = ["title"]
    ordering = ["-created_at"]
    list_per_page = 20
