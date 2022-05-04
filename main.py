from typing import Optional
from fastapi import FastAPI
from APIMusicale.main import getRandomTrackArtist

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"message": "Salut, monde !"}


@app.get("/random/{name_artist}")
def getTrackArtist(name_artist: Optional[str]) -> dict:
    return getRandomTrackArtist(name_artist)
