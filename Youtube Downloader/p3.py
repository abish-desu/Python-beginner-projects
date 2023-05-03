from pytube import YouTube
link = "https://youtu.be/Eu5dbUcu6hI"
yv = YouTube(link)
video = yv.streams.all()
vid = list(enumerate(video))
for i in vid:
    print(i)
print()
strm = int(input("enter : "))
video[strm].download()
print("success")
