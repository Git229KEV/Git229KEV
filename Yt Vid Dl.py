import pytube
url = 'https://www.youtube.com/watch?v=7BXJIjfJCsA'
my_video = pytube.YouTube(url)
stream = my_video.streams.get_by_itag(22)
print("Downloading...")
stream.download(filename='test')
print("Done")
