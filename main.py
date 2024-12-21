from client.createPlaylist.getPlaylist import getPlaylist
from client.getTrack import getTrack

def printOptions():
    print("What do you want ?")
    print("1) Get a playlist")
    print("2) Get a song from an artist")
    print("3) Lauch the 'Rudy' scenario")

printOptions()
x = input()
if "1" == x:
    print('Name of the file used:')
    name = input()
    print('Number of songs desired:')
    number = input()
    print(getPlaylist(name, number))
elif "2" == x:
    print("Artist's name:")
    name = input()
    print(getTrack(name))
elif "3" == x:
    print("'Rudy' scenario launched")
    print(getPlaylist("rudy.json", 20))
else:
    print("This option isn't available yet")
    printOptions()
