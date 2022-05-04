from client.createPlaylist.getPlaylist import getPlaylist
from client.getTrack import getTrack

print("What do you want ?")
print("1) Get a playlist")
print("2) Get a song from an artist")
print("3) Lauch the 'Rudy' scenario")
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
    print(getPlaylist("rudy.json", 20))
