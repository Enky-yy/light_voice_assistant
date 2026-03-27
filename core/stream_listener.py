import sounddevice as sd
import queue

# ✅ GLOBAL QUEUE (IMPORTANT)
audio_queue = queue.Queue()


def get_input_device():
    devices = sd.query_devices()

    for i, d in enumerate(devices):
        if d['max_input_channels'] > 0:
            return i

    raise RuntimeError("No input device found")


def audio_callback(indata, frames, time, status):
    if status:
        print("Audio status:", status)

    audio_queue.put(indata.copy())


def start_stream():
    device_index = 12

    device_info = sd.query_devices(device_index, 'input')
    samplerate = int(device_info['default_samplerate'])

    print(f"Using device {device_index} @ {samplerate} Hz")

    stream = sd.InputStream(
        device=device_index,
        samplerate=samplerate,
        channels=1,
        callback=audio_callback,
        blocksize=1024
    )

    stream.start()
    return stream, samplerate