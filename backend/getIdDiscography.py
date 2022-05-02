import requests


def getIdDiscography(idArtist: int):
    requete = requests.get(
        "https://theaudiodb.com/api/v1/json/{APIKEY}/album.php?i=" + str(
			idArtist))
    liste_info_album = requete["album"]
    liste_id = []
    for i in len(liste_info_album):
		liste_id.append(liste_info_album[i]["idAlbum"])
	return liste_id
