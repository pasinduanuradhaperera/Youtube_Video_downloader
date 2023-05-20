from pytube import YouTube as Y #imoprt pytube
from sys import argv

link = argv[1]
yt = Y(link)
print("Title: ",yt.title)
print("Vievs: ", yt.views)

yD = yt.streams.get_highest_resolution()
yD.download('./downloads') #whatever you like to save downloaded video


