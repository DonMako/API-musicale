from typing import Optional
from fastapi import FastAPI
from backend.getRandomTrackArtist import getRandomTrackArtist

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Salut, monde !"}


@app.get("/random/{artist_name}")
def get_all_words(artist_name: Optional[str]):
    return getRandomTrackArtist(artist_name)
