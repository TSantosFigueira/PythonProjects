#tutorial: https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97
#documentation: https://python-pytube.readthedocs.io/en/latest/index.html

from pytube import YouTube

# todo: create a user inteface to get the link
video_url = input('Please, paste the link from the video: ')
yt = YouTube(video_url)

print('Here are some details about the video you selected')

#video details
print('Title: {}'.format(yt.title))
print("Total views: " + str(yt.views))
print('Rating: ' + str(yt.rating))

print('\nProceeding with download...')
video = yt.streams.get_highest_resolution()

# todo: let user pick download path
video.download()

print('Download completed')