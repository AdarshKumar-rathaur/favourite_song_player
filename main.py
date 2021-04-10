import webbrowser
import random

def listToString(s):
	str1 = ""
	for ele in s:
		str1 += ele
	return str1

a_playlist = open("playlist.txt", "r")
list_of_songs = []
for line in a_playlist:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_songs. append(line_list)
a_playlist.close()
song = random.choice(list_of_songs)

r_song = (listToString(song))
webbrowser.open(r_song)