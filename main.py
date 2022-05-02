import random
from typing import Optional
from fastapi import FastAPI
from backend.getTracksArtist import getTracksArtist

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"message": "Salut, monde !"}


@app.get("/random/{name_artist}")
def getRandomTrackArtist(name_artist: Optional[str]) -> dict:
    list_tracks = getTracksArtist(name_artist)
    random_number = random.randint(0, len(list_tracks) - 1)
    return list_tracks[random_number]

# "https://" + str(self.host) + ":" + str(self.port) + "/random/" + str(daft_punk) -> getRandomTrackArtist("daft punk")
