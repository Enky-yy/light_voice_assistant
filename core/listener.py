from faster_whisper import WhisperModel
import numpy as np

model = WhisperModel("base", compute_type="int8")  # fast

from scipy.signal import resample

def resample_audio(audio, original_sr, target_sr=16000):
    num_samples = int(len(audio) * target_sr / original_sr)
    return resample(audio, num_samples)

def transcribe(audio_data):
    segments, _ = model.transcribe(audio_data, beam_size=1)

    text = ""
    for segment in segments:
        text += segment.text

    return text.lower()