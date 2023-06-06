import os
from moviepy.editor import *
# import tqdm
from tqdm import tqdm, trange


if __name__ == '__main__':

    video = VideoFileClip("./Videos/--playlist/野火F407开发板-霸天虎视频-【入门篇】 (P2. 4-如何使用串口下载程序（第1集）—软件操作演示).flv")    # 讀取影片
    output = video.copy()
    output.write_videofile(f"output.{'mp4'}", remove_temp=True, codec="libx264", audio_codec="aac")