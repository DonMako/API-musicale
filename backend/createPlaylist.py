import json
import random
from backend.getIdArtist import getIdArtist
from backend.getIdDiscography import getIdDiscography
from backend.getLyricsSong import getLyricsSong
from backend.getYTLink import getYTLink


def createPlaylist(taille_playlist: int, fichier: json):
    ajout_nb_recherche(taille_playlist, fichier)
    for artiste in fichier:
        liste_pistes = recup_liste_pistes(
            getIdDiscography(getIdArtist(artiste["artiste"])))
        pistes_selectionnees = []
        for i in artiste["nombre_recherche"]:
            ind = random.randrange(0, len(liste_pistes))
            pistes_selectionnees.append(liste_pistes[ind])
        artiste["liste_pistes"] = pistes_selectionnees
    playlist = []
    for artiste in fichier:
        for piste in artiste["liste_pistes"]:
            chanson = {}
            chanson["artist"] = artiste["artiste"]
            chanson["title"] = piste["titre"]
            chanson["suggested_youtube_url"] = getYTLink(
                getIdArtist(artiste["artiste"]), piste["idTrack"])
            chanson["lyrics"] = getLyricsSong(
                artiste["artiste"], piste["titre"])
            playlist.append(chanson)
    return playlist
