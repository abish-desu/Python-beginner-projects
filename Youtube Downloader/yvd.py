from pytube import YouTube
link = "https://www.youtube.com/watch?v=iMuZRXsE7KI"     # link of the video to download
youtube_1 = YouTube(link)

# print(youtube_1.title)                    # Youtube Title
# print(youtube_1.thumbnail_url)            # Youtube thumbnail

videos = youtube_1.streams.all()            # gives streaming info of the video
vid = list(enumerate(videos))               # stores streaming info on list
for i in vid:                       
    print(i)
print()

strm = int(input("enter : "))              # download videos or audio from the list by entering correponding indexing number of the video
videos[strm].download()
print("Successfully Downloaded")                      
 



