from music.models import Song


class SongService(object):
    _song_model = Song

    @classmethod
    def get_all_artists(cls, **kwargs):
        return cls._song_model.objects.filter(**kwargs).order_by("-created_at")
