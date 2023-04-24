from pytube import YouTube

# function for downloading videos
def download_video(url):
  video = YouTube(url)
  stream = video.streams.get_highest_resolution()
  stream.download()

# function for downloading audios
def download_audio(url):
  video = YouTube(url)
  stream = video.streams.filter(only_audio=True).first()
  stream.download()
