# core/wake_word.py

import numpy as np
import sounddevice as sd
from openwakeword.model import Model
from core.stream_listener import start_stream

# Load model (pretrained)
model = Model()

stream, samplerate = start_stream()

SAMPLE_RATE = samplerate
CHUNK_SIZE = 1280  # ~80ms audio

def listen_for_wake_word():
    print("Listening for wake word (Jarvis)...")

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
        blocksize=CHUNK_SIZE
    ) as stream:

        while True:
            audio, _ = stream.read(CHUNK_SIZE)
            audio = audio.flatten()

            # Convert to float32 (required)
            audio = audio.astype(np.float32) / 32768.0

            # Run prediction
            prediction = model.predict(audio)

            print(prediction)


            # Check score
            score = prediction["hey_jarvis"]

            if score > 0.6:   # threshold (tune this)
                print(f"Wake word detected! Score: {score:.2f}")
                return True