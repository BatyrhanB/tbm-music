from music.models import Album


class AlbumService(object):
    _album_model = Album

    @classmethod
    def get_all_artists(cls, **kwargs):
        return cls._album_model.objects.filter(**kwargs).order_by("-created_at")