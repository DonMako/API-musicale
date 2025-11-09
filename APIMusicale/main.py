import random
from typing import List
from fastapi import FastAPI
import uvicorn
from AudioDB import AudioDB

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"message": "Salut, monde !"}


@app.get("/random/{name_artist}")
def getRandomTrackArtist(name_artist: str) -> List[dict]:
    id_artist = AudioDB.getIdArtist(name_artist)
    list_id_albums = AudioDB.getIdDiscography(id_artist)
    list_tracks = []
    for id_album in list_id_albums:
        list_tracks = list_tracks + AudioDB.getTracksAlbum(id_album)
    for track in list_tracks:
        track["name_artist"] = name_artist
        track["suggested_youtube_url"] = AudioDB.getYTLink(
            id_artist, track["id_track"])
        track["lyrics"] = AudioDB.getLyricsSong(name_artist, track["title"])
        del track["id_track"]
    random_number = random.randint(0, len(list_tracks) - 1)
    return list_tracks[random_number]


if __name__ == "__main__":
    uvicorn.run(app)
