from __future__ import unicode_literals
import youtube_dl


ydl_opts = {}
while True:
    choice = input("""please choose what you want to do:
    1)Youtube MP3 Download
    2)Youtube MP4 Download
    3)Exit""")
    if choice == '1':
        video_url = input("please enter video url:")
        video_info = youtube_dl.YoutubeDL().extract_info(url = video_url, download=False)
        file_name = f"{video_info['title']}.mp3"
        settings = {
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':file_name,
        }
        with youtube_dl.YoutubeDL(settings) as ydl:
            ydl.download([video_info['webpage_url']])
        print(f"downloaded... {file_name}")
    elif choice == '2':
        video_url = input("please enter video url:")
        video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
        file_name = f"{video_info['title']}.mp4"
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"downloaded... {file_name}")
    elif choice == '3':
        print("exit")
        break

#neganwashere