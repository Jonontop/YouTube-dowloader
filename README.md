# This is a simple youtube video/audio downloader in slovenian language

you can export files in .mp3 and .mp4 file format.

 
## Terminal Version
```py

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

```


GUI and Web version will be uploaded soon!
