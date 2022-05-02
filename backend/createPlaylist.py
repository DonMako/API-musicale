import json
from backend.addNumberSearches import addNumberSearches
from backend.getIdArtist import getIdArtist
from backend.getRandomTrackArtist import getRandomTrackArtist
from backend.getLyricsTrack import getLyricsTrack
from backend.getYTLink import getYTLink


def createPlaylist(len_playlist: int, file: json):
    addNumberSearches(len_playlist, file)
    for artist in file:
        list_tracks_selected = []
        for i in artist["numberSearches"]:
            track = getRandomTrackArtist(artist["artiste"])
            if track not in list_tracks_selected:
                list_tracks_selected.append(track["title"])
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
