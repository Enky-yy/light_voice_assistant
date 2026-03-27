# import sounddevice as sd
# for i, d in enumerate(sd.query_devices()):
#     print(i, d['name'], "| inputs:", d['max_input_channels'])


import numpy as np
import sounddevice as sd
from openwakeword.model import Model
from core.stream_listener import start_stream

# Load model (pretrained)
model = Model()
