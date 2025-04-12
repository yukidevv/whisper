import whisper
from whisper.utils import get_writer
import yt_dlp as youtube_dl
from flask import Flask
from flask import render_template

app = Flask(__name__)
output_dir = 'toTxt'

def url_input():
  print("URL",end=':')
  return input()

def get_ydl_otps():
  ydl_opts={
    'format': 'bestaudio/best', # 音声を出力する
    'outtmpl': 'data/%(uploader_id)s/%(id)s.%(ext)s',  #チャンネルID/
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
    }],
  }
  return ydl_opts

def exec_download_audio(url, opts):
  with youtube_dl.YoutubeDL(opts) as ydl:
    ydl.download(url)

#一旦これで
@app.route("/")
def main():
#   url = url_input()
#   exec_download_audio(url, get_ydl_otps())
  return render_template('index.html')

#whisper
# model = whisper.load_model("small")
# result = model.transcribe("./data/Cu-IMFl37LA.mp3")
# json_writer = get_writer("json", output_directory)
# json_writer(result, input)