# whisper
Youtubeのvlog系や配信系の動画をテキストだけで読みたくて作りました  
youtubeの文字起こしだと全文を一気には読めないよね    
youtubeの動画の文字起こしを行い、全文を取得します  
今は【CPUONLY】  
使用方法は以下
1. 対象動画のリンクを貼り付け
2. Whisper用のモデルを選択
3. 実行
4. 文字起こし結果を表示

# 使用技術等
- python3.12.3
- Flask
- yt-dlp
- OpenAI Whisper

# 環境構築
```
$ pip install -r requirements.txt
```
# 使用方法
```
$ python3 main.py
```
http://127.0.0.1:5000
にアクセス