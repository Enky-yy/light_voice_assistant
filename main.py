from core.stream_listener import start_stream, audio_queue
from core.vad import is_speech
from core.listener import transcribe , resample_audio
from core.wake_word import listen_for_wake_word
from core.brain import get_intent
from core.executor import execute
from core.speaker import speak

import numpy as np
import time

def run():
    stream, samplerate = start_stream()

    print("System ready...")

    while True:
        # 1. WAIT FOR WAKE WORD
        listen_for_wake_word()

        speak("Yes?")

        frames = []
        silence_counter = 0

        # 2. CAPTURE SPEECH IN REAL-TIME
        while True:
            if not audio_queue.empty():
                chunk = audio_queue.get()
                chunk = chunk.flatten()

                if is_speech(chunk):
                    frames.append(chunk)
                    silence_counter = 0
                else:
                    silence_counter += 1

                # stop after silence
                if silence_counter > 10:
                    break

        if len(frames) == 0:
            continue

        audio_data = np.concatenate(frames)

        audio_data = resample_audio(audio_data, samplerate, 16000)

        command = transcribe(audio_data)

        # 3. TRANSCRIBE FAST
        command = transcribe(audio_data)
        print("User:", command)

        # 4. INTENT + EXECUTION
        intent = get_intent(command)
        response = execute(intent, command)

        # 5. SPEAK (non-blocking later)
        speak(response)

if __name__ == "__main__":
    run()