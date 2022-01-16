from pytube import YouTube
# DOWNLOAD_FOLDER = "Users/srini/OneDrive/Desktop/New folder"
# video_url = "https://youtu.be/Cn-o7RzUPpU"
# video_obj = YouTube(video_url)
# stream = video_obj.streams.get_highest_resolution()
# stream.download(DOWNLOAD_FOLDER)

url = 'https://youtu.be/VCQvgWKRMLU'
my_video = YouTube(url)
print("*********************Video Title************************")
# get Video Title
print(my_video.title)

print("********************Tumbnail Image***********************")
# get Thumbnail Image
print(my_video.thumbnail_url)

print("********************Download video*************************")
# get all the stream resolution for the
for stream in my_video.streams:
    print(stream)

# set stream resolution
my_video = my_video.streams.get_highest_resolution()

# or
#my_video = my_video.streams.first()

# Download video
my_video.download()
