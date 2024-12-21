from pytube import YouTube
import os

def download_mp3(youtube_url, output_dir="downloads"):
    yt = YouTube(youtube_url)
    stream = yt.streams.filter(only_audio=True).first()
    output_path = stream.download(output_dir)

    # Convert to MP3
    base, ext = os.path.splitext(output_path)
    mp3_path = base + ".mp3"
    os.rename(output_path, mp3_path)
    return mp3_path
