# API-musicale

Author : MACAUX Lucas

## What is an API-musicale ?

You live in Rennes and you want to sing in Musikam, the biggest french karaoke-club, but you don't know what songs to perform ?

Don't worry, the API-musicale is here for **you** !

You just need to indicate a list of singers/musicians you like, and how much do you like them, and **HOP!** the API-musicale makes your evening a ✨ _magical moment_ ✨ !

## Description of the project

The project consists of the realization of a musical API, which is based on the use of 2 external APIs: [AudioDB](https://www.theaudiodb.com/api_guide.php) and [Lyricsovh](https://lyricsovh.docs.apiary.io/).

This musical API is able to:
* randomly get the song of a given artist as input
* create a playlist of _x_ songs from a file following the pattern of the _rudy.json_ file, with _x_ a number chose by the user.

## Quick Start

### Installation
```
git clone https://github.com/DonMako/API-musicale
cd API-musicale
pip install -r requirements.txt
```

### Running the application
First, run the API.
```
cd APIMusicale
python main.py
```
Then, in an other terminal:
```
python main.py
```

## Simple macro architecture diagram of the application

```mermaid
  info
```

```mermaid
flowchart LR
    A(User) -->|json, int| B(Client)
    B -->|json| A
    B -->|HTTPS requests| C{API-musicale}
    C -->|HTTPS response| B
    C -->|HTTPS requests| D(AudioDB)
    C -->|HTTPS requests| E(LyricsOvh)
    D -->|HTTPS response| C
    E -->|HTTPS response| C
```

## To run some tests

For the moment, only one test is coded into the project.

To run this test:
```
cd tests
python testAPI.py
```
