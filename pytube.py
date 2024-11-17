import pytubefix as pytube

vnos_type = input("Vnesi ali želiš mp3 (zvok) ali mp4 (zvok + video): ")
vnos = input("Vnesi URL za video: ")
place = input("Vnesi datotečno pot do želene mape: ")

yt = pytube.YouTube(vnos)

print(f"Naslov videa: {yt.title} \nPrenašanje...")

yt.streams.filter(only_audio=True).first().download(place) if vnos_type == "mp3" else yt.streams.get_highest_resolution().download(place)

print("Prenos končan!")
