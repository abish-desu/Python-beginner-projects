
from pytube import YouTube
link = "https://www.youtube.com/watch?v=iMuZRXsE7KI"
yv = YouTube(link)
video = yv.streams.all()
vid = list(enumerate(video))
for i in vid:
    print(i)
print()
strm = int(input("enter : "))
video[strm].download()
print("successful")