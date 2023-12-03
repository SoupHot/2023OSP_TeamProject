from fastapi import FastAPI
from fastapi.responses import FileResponse
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import torch
import scipy
import time

app = FastAPI()
# uvicorn api:app --reload --host=0.0.0.0 --port=7342

@app.get("/")
def test():
    return 'OSP Project API TEST(DEMO)'

@app.get("/music-gen/{prompt}/{duration}",)
def music_gen(prompt: str, duration: int):
    start_time = time.time()
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
    device = "cuda:3" if torch.cuda.is_available() else "cpu"
    model.to(device)

    inputs = processor(
        text=[prompt],
        padding=True,
        return_tensors="pt",
    )

    max_new_tokens = model.config.audio_encoder.frame_rate * duration

    audio_values = model.generate(**inputs.to(device), max_new_tokens=max_new_tokens)
    sampling_rate = model.config.audio_encoder.sampling_rate
    file_path = "/home/wook/fastAPI/musicgen_out.wav"
    scipy.io.wavfile.write(file_path, rate=sampling_rate, data=audio_values[0, 0].cpu().numpy())
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"실행 시간: {execution_time}초")

    return FileResponse(file_path, media_type='audio/wav', filename="musicgen_out.wav")