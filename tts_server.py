from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from TTS.api import TTS
import io

app = FastAPI()

# Hugging Face 모델 실시간 로드
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

@app.get("/tts")
def generate_tts(text: str = Query(...)):
    audio_fp = io.BytesIO()
    tts.tts_to_file(text=text, file_path=audio_fp, speaker="alloy")  # alloy는 예시
    audio_fp.seek(0)
    return StreamingResponse(audio_fp, media_type="audio/mpeg")
