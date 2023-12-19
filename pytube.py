import pytube
from pytube import YouTube
import os


vnos_type= input("Vnesi ali želiš mp3(zvok) ali mp4(zvok + video): ")
vnos = input("Vnesi URL za video: ")
place = input("Vnesi datotečno pot do želene mape: ")

yt = pytube.YouTube(vnos)

if (vnos_type == "mp3"):
    video = yt.streams.filter(only_audio=True).first()
else:
    video = yt.streams.first()


print(yt.title)

print("prenašanje...")

video.download(place)
