# Video Downloader with Terminal and Tkinter GUI

This code allows users to download videos from YouTube using either a terminal-based interface or a graphical user interface (GUI) built with Tkinter.

## Terminal Code

- Users input whether they want to download the video as an mp3 (audio only) or mp4 (audio and video).
- They then provide the URL of the video and the directory path where they want to save the downloaded file.
- The Pytube library is used to interact with YouTube and download the video accordingly.
- The downloaded video is saved to the specified directory.

## Pythinker Code (Tkinter GUI)

- Users interact with a graphical interface where they input the desired download type (mp3 or mp4), the video URL, and the destination directory.
- Upon clicking the download button, the program retrieves the values from the entry fields and initiates the download process using Pytube.
- The interface also displays a confirmation message upon successful completion of the download.

### Key Components:

- Entry fields for users to input the download type, video URL, and destination directory.
- A download button that triggers the download process.
- Labels to display the purpose of each input field.
- The GUI window is centered on the screen for better user experience.

## Note

- Both versions of the code utilize the Pytube library to interact with YouTube and download videos.
- The terminal version is suitable for users comfortable with command-line interfaces, while the Tkinter GUI provides a more user-friendly experience for those who prefer graphical interfaces.


 
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
## Application Version V1.0
```py
import pytube
import os
from tkinter import *
import tkinter as tk


def main():

    # Access the values from the Entry widgets
    mp3_mp4_value = vnos_type.get()
    url_value = vnos.get()
    path_value = place.get()

    # Use the values as needed (for now, just print them)
    print("mp3/mp4:", mp3_mp4_value)
    print("URL:", url_value)
    print("PATH:", path_value)


    yt = pytube.YouTube(vnos.get())

    if (vnos_type == "mp3"):
        video = yt.streams.filter(only_audio=True).first()
    else:
        video = yt.streams.first()

    print(yt.title)

    print("prenašanje...")

    video.download(place.get())

    x = Label(root, text="Končano")
    x.pack()
    x1 = Label(root, text="Vaš posnetek: "+yt.title+" je bil uspešno prenešen!")
    x1.pack()

    print("Končano!")



# Create the Tkinter window
root = tk.Tk()
root.geometry('800x400')  # Adjust the window size as needed
root.title('Downloader')

# Declare variables to store the values
mp3_mp4_var = tk.StringVar()
url_var = tk.StringVar()
path_var = tk.StringVar()

# Label and Entry for mp3/mp4
vnosTypeTitle = Label(root, text="mp3/mp4: ", font=("Arial", 20))
vnosTypeTitle.grid(row=0, column=0, pady=10)

vnos_type = Entry(root, font=("Arial", 20), textvariable=mp3_mp4_var, width=30)
vnos_type.grid(row=0, column=1, pady=10)

# Label and Entry for URL
vnosTitle = Label(root, text="URL: ", font=("Arial", 20))
vnosTitle.grid(row=1, column=0, pady=10)

vnos = Entry(root, font=("Arial", 20), textvariable=url_var, width=30)
vnos.grid(row=1, column=1, pady=10)

# Label and Entry for PATH
placeTitle = Label(root, text="PATH: ", height=1, font=("Arial", 20))
placeTitle.grid(row=2, column=0, pady=10)

place = Entry(root, font=("Arial", 20), textvariable=path_var, width=30)
place.grid(row=2, column=1, pady=10)

# Download button
download_button = Button(root, text="Download", command=main, height=5, width=25, font=("Arial", 20))
download_button.grid(row=3, column=0, columnspan=2, pady=20)

# Center the interface
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - root.winfo_width()) // 2
y = (screen_height - root.winfo_height()) // 2
root.geometry("+{}+{}".format(x, y))

# Start the Tkinter event loop
root.mainloop()


```


Web version will be uploaded soon!
