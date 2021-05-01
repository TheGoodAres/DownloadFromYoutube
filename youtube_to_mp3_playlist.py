from moviepy.editor import *
import os, shutil
from pytube import Playlist

def get_mp3():
    playlist_url = input("Enter a YouTube playlist link: ")
    playlist = Playlist(playlist_url)
    output = "mp3"
    print("Converting...")
    for i in playlist.videos:
        mp4 = i.streams.get_highest_resolution().download()
        mp3 = mp4.split(".mp4", 1)[0] + f".{output}"

        video_clip = VideoFileClip(mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3)

        audio_clip.close()
        video_clip.close()

        os.remove(mp4)
        shutil.move(mp3, "")  # Replace this with your own output directory


get_mp3()
