# importing module
import youtube_dl
#


# import youtube_dl
import time
from selinium_script import video_list, download

ydl_opts = {}
link_list = list(video_list())
print(len(link_list))
print(link_list)


for i in link_list:
    download(i)




def playlist_downloader(link):
    ydl = youtube_dl.YoutubeDL({'dump_single_json': True,
                                'extract_flat': True})

    with ydl:
        result = ydl.download([
            link])

    print(result)

# Todo: some videos not downloading issue
# Todo: remove the downloaded video from watch later playlist