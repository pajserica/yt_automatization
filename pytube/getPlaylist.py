import re
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/watch?v=7VbPiUSXzLI&list=PL_JdwZWnDhAVR_F6-B-ZIMOSYOJlOsSUd')   
DOWNLOAD_DIR = r'C:\Users\PAJSER-PC\Desktop\videiSpanski'
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")    
print(len(playlist.video_urls))    
  
for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(DOWNLOAD_DIR)

print("Download finished!")
