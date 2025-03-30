import whisper

model = whisper.load_model("small")
result = model.transcribe("./data/output.wav")
print(result["text"])
