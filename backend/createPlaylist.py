import json
from typing import List
from frontend.addNumberSearches import addNumberSearches
from backend.selectSongsFromFile import selectSongsFromFile
from backend.AudioDB.getYTLink import getYTLink
from backend.AudioDB.getIdArtist import getIdArtist
from backend.LyricsOvh.getLyricsSong import getLyricsSong


def createPlaylist(file: json, len_playlist: int) -> List[dict]:
    addNumberSearches(file, len_playlist)
    playlist, list_songs = [], selectSongsFromFile(file)
    for song in list_songs:
        dico = {}
        dico["artist"] = song["name_artist"]
        dico["title"] = song["title"]
        dico["suggested_youtube_url"] = getYTLink(
            getIdArtist(song["name_artist"]), song["id_track"])
        dico["lyrics"] = getLyricsSong(
            song["name_artist"], song["title"])
        playlist.append(dico)
    return playlist
