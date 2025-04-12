import whisper
from whisper.utils import get_writer
import yt_dlp as youtube_dl

def url_input():
  print("URL",end=':')
  return input()

def get_ydl_otps():
  ydl_opts={
    'format': 'bestaudio/best', # 音声のみ
    'outtmpl': '%(id)s.%(ext)s',  # 動画IDをファイル名に
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
    }],
  }
  return ydl_opts

def exec_download_audio(url, otps):
  with youtube_dl.YoutubeDL(opts) as ydl:
    ydl.download(url)

url = url_input()
opts = get_ydl_otps()
exec_download_audio(url, opts)

# output_directory = "toTxt/"
# input = "./data/Cu-IMFl37LA.mp3"

# model = whisper.load_model("small")
# result = model.transcribe("./data/Cu-IMFl37LA.mp3")
# json_writer = get_writer("json", output_directory)
# json_writer(result, input)

