import random
from typing import List
from fastapi import FastAPI
import uvicorn
from AudioDB.getIdArtist import getIdArtist
from AudioDB.getIdDiscography import getIdDiscography
from AudioDB.getTracksAlbum import getTracksAlbum
from AudioDB.getYTLink import getYTLink
from LyricsOvh.getLyricsSong import getLyricsSong

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"message": "Salut, monde !"}


@app.get("/random/{name_artist}")
def getRandomTrackArtist(name_artist: str) -> List[dict]:
    id_artist = getIdArtist(name_artist)
    list_id_albums = getIdDiscography(id_artist)
    list_tracks = []
    for id_album in list_id_albums:
        list_tracks = list_tracks + getTracksAlbum(id_album)
    for track in list_tracks:
        track["name_artist"] = name_artist
        track["suggested_youtube_url"] = getYTLink(
            id_artist, track["id_track"])
        track["lyrics"] = getLyricsSong(name_artist, track["title"])
        del track["id_track"]
    random_number = random.randint(0, len(list_tracks) - 1)
    return list_tracks[random_number]


if __name__ == "__main__":
    uvicorn.run(app)
