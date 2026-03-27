import webrtcvad
import numpy as np

vad = webrtcvad.Vad(2)

def is_speech(audio_chunk):
    audio_bytes = (audio_chunk * 32768).astype("int16").tobytes()
    return vad.is_speech(audio_bytes, 16000)