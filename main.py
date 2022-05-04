from client.createPlaylist.getPlaylist import getPlaylist
from client.getTrack import getTrack

print("What do you want ?\n1) Get a playlist\n2) Get a song from an artist\n3) Lauch the 'Rudy' scenario")
x = input()
if "1" in x:
    print('Name of the file used:')
    name = input()
    print('Number of songs desired:')
    number = input()
    print(getPlaylist(name, number))
elif "2" in x:
    print("Artist's name:")
    name = input()
    print(getTrack(name))
else:
    print(getPlaylist(rudy.json, 20))