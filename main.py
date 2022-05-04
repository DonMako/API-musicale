from client.createPlaylist.getPlaylist import getPlaylist
from client.getTrack import getTrack

print('What do you want ?\n1) Get a playlist\n2) Get a song from an artist')
x = input()
if x == "1":
    print('Name of the file used:')
    name = input()
    print('Number of songs desired:')
    number = input()
    print(getPlaylist(name, number))
else:
    print("Artist's name:")
    name = input()
    print(getTrack(name))
