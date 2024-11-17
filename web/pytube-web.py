import pytubefix as pytube
from flask import Flask, request, send_file, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    vnos_type = request.form['format']  # Get the format (mp3 or mp4) from radio button
    vnos = request.form['url']  # Get the video URL

    # Create a download path in the server's current directory
    download_path = "downloads"
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    yt = pytube.YouTube(vnos)

    # Set file name and download based on the type selected
    if vnos_type == "mp3":
        audio_stream = yt.streams.filter(only_audio=True).first()
        file_path = os.path.join(download_path, f"{yt.title}.mp3")
        audio_stream.download(output_path=download_path, filename=f"{yt.title}.mp3")
    else:
        video_stream = yt.streams.get_highest_resolution()
        file_path = os.path.join(download_path, f"{yt.title}.mp4")
        video_stream.download(output_path=download_path, filename=f"{yt.title}.mp4")

    # Serve the file to the user
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
