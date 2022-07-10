import time
from selinium_script import video_list, download

time.sleep(3)
link_list = list(video_list())
print(len(link_list))
print(link_list)

for i in link_list:
    length = len(i)
    download(i)

#Todo: sometimes unable to click, save to watch later button.()
#Todo: check the whach later if it is already unticked, if it is already unticked leave it.
#Todo: some times ad is interupting.
#Todo:some times the save button is clicked twice. and the menu closes before clicking the watch later button.
