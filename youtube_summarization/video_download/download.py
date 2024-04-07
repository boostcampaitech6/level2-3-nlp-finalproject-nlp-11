from pytube import YouTube
import re

def download_video(video_url):
    DOWNLOAD_DIR = r"../stt"
    yt = YouTube(video_url)
    title = yt.title
    title = re.sub('[^\w\d\s.,]','', title)
    title = re.sub('\s','_', title)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(DOWNLOAD_DIR, filename=f'{title}.mp4')

    f = open('../text_summarization/title.txt', 'w')
    f.write(title)
    f.close()
