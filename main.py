from pytube import YouTube
import pyautogui as pg

link = pg.prompt(title="Youtube video downloader", text="Enter the youtube link.")      # Takes a vaue to get the youtube link.
yt = YouTube(link)

print("Title: ", yt.title)                          # Gets the title of the video
print("Views: ", yt.views)                          # Gets the no. of views of the video.

ys = yt.streams.get_audio_only()
yd = yt.streams.get_highest_resolution()

print(ys)

ans = input("Audio or video(a/v): ")
if ans == "a":
    ys.download()                                   # Downloads an audio (But you might have to rename the file extention to .mp3)
if ans == "v":
    yd.download()                                   # Downloads a video