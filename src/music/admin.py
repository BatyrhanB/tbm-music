from django.contrib import admin


from music.models import Artist


@admin.register(Artist)
class ArtistADmin(admin.ModelAdmin):
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
