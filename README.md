# Schéma d'architecture

graph TD
    A(User) -->|json| B(Client)
    B -->|json| A
    B -->|HTTPS requests| C{API-musicale}
    C -->|HTTPS requests| D(AudioDB)
    C -->|HTTPS requests| E(LyricsOvh)
    D -->|HTTPS requests| C
    E -->|HTTPS requests| C
