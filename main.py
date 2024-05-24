from pytube import YouTube

link = input("Enter the youtube link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

ys = yt.streams.get_audio_only()

yd = yt.streams.get_highest_resolution()

ans = input("Audio or video(a/v): ")
if ans == "a":
    ys.download()
if ans == "v":
    yd.download()