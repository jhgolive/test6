import requests

def tts_hf(text):
    url = "https://api-inference.huggingface.co/models/coqui/tts-ko-ft-multilingual-v1"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": text}
    r = requests.post(url, headers=headers, json=payload)
    if r.status_code == 200:
        with open("tts.mp3", "wb") as f:
            f.write(r.content)
    else:
        print("TTS 실패:", r.status_code, r.text)
