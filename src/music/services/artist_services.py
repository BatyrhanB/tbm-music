from music.models import Artist


class ArtistService(object):
    _artist_model = Artist

    @classmethod
    def get_all_artists(cls, **kwargs):
        return cls._artist_model.objects.filter(**kwargs).order_by("-created_at")
