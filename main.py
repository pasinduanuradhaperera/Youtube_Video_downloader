from pytube import YouTube as Yo  # import pytube
from sys import argv


def download(link):
    yt = Yo(link)
    print("Title: ", yt.title)  # display title
    print("Vievs: ", yt.views)  # display views

    yD = yt.streams.get_highest_resolution()
    yD.download('./downloads')  # whatever you like to save downloaded video
