from pytube import YouTube as Yo  # import pytube
from sys import argv

link = input("Enter Link : ")  # assign the argument to link variable
yt = Yo(link)
print("Title: ", yt.title)  # display title
print("Vievs: ", yt.views)  # display views

yD = yt.streams.get_highest_resolution() 
yD.download('./downloads')  # whatever you like to save downloaded video


