# from __future__ import unicode_literals

# import youtube_dl

# print("Insert the link")

# link = input ("") # 또는 아래와 같이 직접 유튜브 동영상 주소를 파이썬 스크립트 파일에 복사

# # link = "https://youtu.be/gRyJZYOEQ9Y"

# ydl_opts = {

#     'format': 'bestaudio/best',

#     'postprocessors': [{

#         'key': 'FFmpegExtractAudio',

#         'preferredcodec': 'mp3',

#         'preferredquality': '320',

#     }],

# }

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([link])

import moviepy.editor as mp
clip = mp.VideoFileClip("circles.webm")
clip.audio.write_audiofile("audio.mp3")