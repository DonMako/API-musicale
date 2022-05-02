import json
import random
from backend.addNumberSearches import addNumberSearches
from backend.getIdArtist import getIdArtist
from backend.getIdDiscography import getIdDiscography
from backend.getLyricsTrack import getLyricsTrack
from backend.getTracksAlbum import getTracksAlbum
from backend.getYTLink import getYTLink


def createPlaylist(len_playlist: int, file: json):
    addNumberSearches(len_playlist, file)
    for artiste in file:
        list_tracks_album = getTracksAlbum()
        pistes_selectionnees = []
        for i in artiste["nombre_recherche"]:
            ind = random.randrange(0, len(liste_pistes))
            pistes_selectionnees.append(liste_pistes[ind])
        artiste["liste_pistes"] = pistes_selectionnees
    playlist = []
    for artiste in file:
        for piste in artiste["liste_pistes"]:
            chanson = {}
            chanson["artist"] = artiste["artiste"]
            chanson["title"] = piste["titre"]
            chanson["suggested_youtube_url"] = getYTLink(
                getIdArtist(artiste["artiste"]), piste["idTrack"])
            chanson["lyrics"] = getLyricsTrack(
                artiste["artiste"], piste["titre"])
            playlist.append(chanson)
    return playlist
