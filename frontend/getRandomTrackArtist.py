import random
from backend.getTracksArtist import getTracksArtist


def getRandomTrackArtist(name_artist: str) -> dict:
    list_tracks = getTracksArtist(name_artist)
    random_number = random.randint(0, len(list_tracks) - 1)
    return list_tracks[random_number]
