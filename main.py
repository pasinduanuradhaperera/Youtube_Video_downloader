from pytube import YouTube as Y #imoprt pytube
from sys import argv

link = argv[1] #assign the agrument to link variable 
yt = Y(link)
print("Title: ",yt.title) #display title 
print("Vievs: ", yt.views) #display views 

yD = yt.streams.get_highest_resolution() 
yD.download('./downloads') #whatever you like to save downloaded video


