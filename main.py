from typing import Optional
from fastapi import FastAPI
from frontend.getRandomTrackArtist import getRandomTrackArtist

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    return {"message": "Salut, monde !"}


@app.get("/random/{artist_name}")
def get_all_words(artist_name: Optional[str]) -> dict:
    return getRandomTrackArtist(artist_name)
