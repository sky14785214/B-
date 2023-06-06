import os
from moviepy.editor import *
from os import listdir
from tqdm import tqdm, trange
from os.path import isfile, isdir, join


def download(url,savePath):
    os.system("you-get -o"+ savePath +"--playlist %s" % (url))
    
def flv_path(downloadVideoList,savePath):
    temp = [file for file in downloadVideoList if file.endswith('.flv')]
    fltPath = [savePath+'--playlist/' + file for file in temp]
    print(fltPath[0])
    return fltPath

if __name__ == '__main__':


    savePath = "./Videos/"
    downloadList = []
    '''
    downloadUrl = [
                    "https://www.bilibili.com/video/BV1Vt411X7PK?p=",
                    "https://www.bilibili.com/video/BV1xt411X74L?p=",
                    "https://www.bilibili.com/video/BV16t411D7m3?p="
                    ]
    '''
    
    downloadUrl = "https://www.bilibili.com/video/BV16t411D7m3?p="

    pageEnd = 85
    pageStar = 6
    downloadVideo_temp = listdir(savePath+"--playlist/")

    url_temp = 0
    for i in range(pageStar,pageEnd+1,1):
        downloadList.append(downloadUrl[url_temp]+str(i))
    
    for downNum in tqdm(range(len(downloadList))):
        download(downloadList[downNum],savePath)
        

    downloadFlvPath = flv_path(downloadVideo_temp,savePath+'--playlist/')


    # print(len(downloadList))
    for file in downloadFlvPath:
        video = VideoFileClip("野火F407开发板-霸天虎视频-【入门篇】 (P1. 3-如何用DAP仿真器下载程序).flv")    # 讀取影片
        output = video.copy()
        output.write_videofile(f"output.{'mp4'}", remove_temp=True, codec="libx264", audio_codec="aac")

    # print('ok')