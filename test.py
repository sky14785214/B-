import os
from moviepy.editor import *
# import tqdm
from tqdm import tqdm, trange
def download(url,savePath):
    os.system("you-get --o"+ savePath +"--playlist %s" % (url))
    

if __name__ == '__main__':


    savePath = "./Videos/"
     
                    
 
    download("https://www.bilibili.com/video/BV1Vt411X7PK?p=1",savePath)
        



    # print(len(downloadList))

    # video = VideoFileClip("野火F407开发板-霸天虎视频-【入门篇】 (P1. 3-如何用DAP仿真器下载程序).flv")    # 讀取影片

    # format_list = ['mp4']  # 要轉換的格式清單

    # # 使用 for 迴圈轉換成所有格式
    # for i in format_list:
    #     output = video.copy()
    #     output.write_videofile(f"output.{i}", remove_temp=True, codec="libx264", audio_codec="aac")

    # print('ok')