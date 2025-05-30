import whisper
from whisper.utils import get_writer
import yt_dlp as youtube_dl
from flask import Flask,render_template,jsonify, request
import os

app = Flask(__name__)

def get_ydl_otps():
  ydl_opts={
    'format': 'bestaudio/best', # 音声を出力する
    'outtmpl': 'data/%(uploader_id)s/%(id)s.%(ext)s',
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
    }],
  }
  return ydl_opts

def exec_audio_transcribe(url, selected_model, opts):
  trans_txt = ''
  with youtube_dl.YoutubeDL(opts) as ydl:
    try:
      info = ydl.extract_info(url, download=False)
      downloaded_file = ydl.prepare_filename(info)
      output_absolute_path = os.path.splitext(downloaded_file)[0] + '.mp3'
      ydl.download(url)
      trans_txt = speech_to_txt(output_absolute_path, selected_model)
    except Exception as e:
      print(f"Download error: {e}")
    return trans_txt

def speech_to_txt(audio_dir, selected_model):
  try:
    print(audio_dir)
    model = whisper.load_model(selected_model)
    result = model.transcribe(audio_dir)
  except Exception as e:
    print("Whisper execution error:", e)
  return result['text']

@app.route("/")
def main():
  return render_template('index.html')

@app.route("/api/v1/transcribe",methods=['POST'])
def convert_movie_to_txt():
  if request.method == 'POST':
    print(request.json['model'])
    return jsonify({"text": exec_audio_transcribe(request.json['url'], request.json['model'], get_ydl_otps())})

if __name__ == "__main__":
  app.run(debug=True)
